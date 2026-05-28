# futures-code-search

Offline CLI lookup for China futures product codes. The v1 data is static and
based on the AkShare futures documentation tables updated on 2024-11-18:

https://akshare.akfamily.xyz/data/futures/futures.html

## Usage

From this directory:

```bash
./search RB
./search rb
./search --json IF
./search --list-exchanges
./search --version-source
```

Exact product-code matching is used. Contract codes such as `rb2410` are not
parsed in v1.

You can also run it as a Python module:

```bash
python3 -m futures_code_search RB
```

## Tests

```bash
python3 -m unittest discover -s tests
```
