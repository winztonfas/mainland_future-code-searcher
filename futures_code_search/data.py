from __future__ import annotations

import json
from dataclasses import dataclass
from importlib import resources
from typing import Any


SOURCE_URL = "https://akshare.akfamily.xyz/data/futures/futures.html"
SOURCE_UPDATED = "2024-11-18"


@dataclass(frozen=True)
class FuturesProduct:
    code: str
    display_code: str
    name_cn: str
    exchange_code: str
    exchange_name_cn: str
    listing_date: str
    source_updated: str
    market: str

    @classmethod
    def from_dict(cls, row: dict[str, Any]) -> "FuturesProduct":
        return cls(
            code=row["code"],
            display_code=row["display_code"],
            name_cn=row["name_cn"],
            exchange_code=row["exchange_code"],
            exchange_name_cn=row["exchange_name_cn"],
            listing_date=row["listing_date"],
            source_updated=row["source_updated"],
            market=row["market"],
        )

    def as_dict(self) -> dict[str, str]:
        return {
            "code": self.code,
            "display_code": self.display_code,
            "name_cn": self.name_cn,
            "exchange_code": self.exchange_code,
            "exchange_name_cn": self.exchange_name_cn,
            "listing_date": self.listing_date,
            "source_updated": self.source_updated,
            "market": self.market,
        }


def _load_payload() -> dict[str, Any]:
    path = resources.files(__package__).joinpath("data/futures_products.json")
    return json.loads(path.read_text(encoding="utf-8"))


def load_products() -> list[FuturesProduct]:
    payload = _load_payload()
    return [FuturesProduct.from_dict(row) for row in payload["products"]]


def load_exchanges() -> list[dict[str, str]]:
    payload = _load_payload()
    return list(payload["exchanges"])


def lookup_product(code: str) -> FuturesProduct | None:
    normalized = code.strip().upper()
    for product in load_products():
        if product.code == normalized:
            return product
    return None
