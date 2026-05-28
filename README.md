# futures-code-search

Offline CLI lookup for China futures product codes. The v1 data is static and
based on the AkShare futures documentation tables updated on 2024-11-18:

https://akshare.akfamily.xyz/data/futures/futures.html

## Usage

From this directory:

```bash
python3 -m futures_code_search RB
python3 -m futures_code_search rb
python3 -m futures_code_search --json IF
python3 -m futures_code_search --list-exchanges
python3 -m futures_code_search --version-source
```

Exact product-code matching is used. Contract codes such as `rb2410` are not
parsed in v1.

## Tests

```bash
python3 -m unittest discover -s tests
```
