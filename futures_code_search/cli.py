from __future__ import annotations

import argparse
import json
import sys
from collections.abc import Sequence

from .data import SOURCE_UPDATED, SOURCE_URL, load_exchanges, lookup_product


def _print_table(headers: Sequence[str], rows: Sequence[Sequence[str]]) -> None:
    widths = [len(header) for header in headers]
    for row in rows:
        for index, cell in enumerate(row):
            widths[index] = max(widths[index], len(cell))

    print("  ".join(header.ljust(widths[index]) for index, header in enumerate(headers)))
    print("  ".join("-" * width for width in widths))
    for row in rows:
        print("  ".join(cell.ljust(widths[index]) for index, cell in enumerate(row)))


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="futures-code-search",
        description="Offline lookup for futures product codes.",
    )
    parser.add_argument("code", nargs="?", help="Exact futures product code, for example RB or IF.")
    parser.add_argument("--json", action="store_true", help="Print lookup result as JSON.")
    parser.add_argument("--list-exchanges", action="store_true", help="List supported exchanges.")
    parser.add_argument("--version-source", action="store_true", help="Show data source and update date.")
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)

    if args.version_source:
        print(f"Source: {SOURCE_URL}")
        print(f"Source table updated: {SOURCE_UPDATED}")
        return 0

    if args.list_exchanges:
        rows = [
            [row["exchange_code"], row["exchange_name_cn"], row["suffix"], row["homepage"]]
            for row in load_exchanges()
        ]
        _print_table(["Exchange", "Chinese Name", "Suffix", "Homepage"], rows)
        return 0

    if not args.code:
        parser.error("code is required unless --list-exchanges or --version-source is used")

    product = lookup_product(args.code)
    if product is None:
        print(f"Not found: {args.code}", file=sys.stderr)
        return 1

    if args.json:
        print(json.dumps(product.as_dict(), ensure_ascii=False, indent=2))
        return 0

    _print_table(
        ["Code", "Chinese Name", "Exchange", "Exchange Name"],
        [[product.display_code, product.name_cn, product.exchange_code, product.exchange_name_cn]],
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
