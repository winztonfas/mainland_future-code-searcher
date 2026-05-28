import contextlib
import io
import json
import unittest

from futures_code_search.cli import main
from futures_code_search.data import lookup_product


class LookupTests(unittest.TestCase):
    def test_known_domestic_codes(self):
        cases = {
            "IF": ("沪深300股指期货", "CFFEX"),
            "SC": ("原油", "INE"),
            "RB": ("螺纹钢", "SHFE"),
            "TA": ("PTA", "CZCE"),
            "JM": ("焦煤", "DCE"),
            "LC": ("碳酸锂", "GFEX"),
        }
        for code, (name_cn, exchange_code) in cases.items():
            with self.subTest(code=code):
                product = lookup_product(code)
                self.assertIsNotNone(product)
                self.assertEqual(product.name_cn, name_cn)
                self.assertEqual(product.exchange_code, exchange_code)

    def test_lookup_is_case_insensitive(self):
        product = lookup_product("rb")
        self.assertIsNotNone(product)
        self.assertEqual(product.code, "RB")

    def test_contract_code_is_not_parsed(self):
        self.assertIsNone(lookup_product("rb2410"))


class CliTests(unittest.TestCase):
    def test_unknown_code_exits_nonzero(self):
        stderr = io.StringIO()
        with contextlib.redirect_stderr(stderr):
            status = main(["XYZ"])
        self.assertEqual(status, 1)
        self.assertIn("Not found: XYZ", stderr.getvalue())

    def test_json_output_has_stable_keys(self):
        stdout = io.StringIO()
        with contextlib.redirect_stdout(stdout):
            status = main(["--json", "IF"])
        self.assertEqual(status, 0)
        payload = json.loads(stdout.getvalue())
        self.assertEqual(payload["code"], "IF")
        self.assertEqual(payload["name_cn"], "沪深300股指期货")
        self.assertEqual(payload["exchange_code"], "CFFEX")
        self.assertEqual(payload["market"], "CN")


if __name__ == "__main__":
    unittest.main()
