# futures-code-search

[中文文档](README_CN.md)

Offline CLI lookup for China futures product codes. The v1 data is static and
based on the AkShare futures documentation tables updated on 2024-11-18:

## Install

Clone the repository:

```bash
git clone https://github.com/winztonfas/mainland_future-code-searcher.git
cd mainland_future-code-searcher
```

Run directly without installing:

```bash
./search RB
```

Or install the `search` command locally:

```bash
python3 -m pip install -e .
search RB
```

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
