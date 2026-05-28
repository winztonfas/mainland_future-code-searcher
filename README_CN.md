# mainland_future-code-searcher

一个本地离线的中国大陆期货品种代码查询工具。输入期货品种代码后，输出对应的中文品种名和交易所。

数据为静态内置，不依赖 AkShare API 运行。v1 数据参考 AkShare 期货文档中 `2024-11-18` 更新的交易所表、金融期货表和商品期货表：

https://akshare.akfamily.xyz/data/futures/futures.html

## 功能

- 本地离线查询，无需联网
- 支持中国大陆主要期货交易所：
  - 中国金融期货交易所 CFFEX
  - 上海期货交易所 SHFE
  - 上海国际能源交易中心 INE
  - 郑州商品交易所 CZCE
  - 大连商品交易所 DCE
  - 广州期货交易所 GFEX
- 默认输出紧凑表格
- 支持 JSON 输出，方便脚本调用

## 安装

先克隆仓库：

```bash
git clone https://github.com/winztonfas/mainland_future-code-searcher.git
cd mainland_future-code-searcher
```

如果只是本地使用，不需要安装依赖，直接运行：

```bash
./search RB
```

如果想把 `search` 安装成系统命令，建议使用 editable install：

```bash
python3 -m pip install -e .
search RB
```

卸载：

```bash
python3 -m pip uninstall futures-code-search
```

## 使用

查询螺纹钢：

```bash
./search rb
```

输出示例：

```text
Code  Chinese Name  Exchange  Exchange Name
----  ------------  --------  -------------
RB    螺纹钢           SHFE      上海期货交易所
```

查询沪深 300 股指期货：

```bash
./search IF
```

JSON 输出：

```bash
./search --json LC
```

查看支持的交易所：

```bash
./search --list-exchanges
```

查看数据来源：

```bash
./search --version-source
```

也可以用 Python module 方式运行：

```bash
python3 -m futures_code_search RB
```

## 匹配规则

当前版本只做品种代码精确匹配，并且忽略大小写。

- `rb` 可以匹配 `RB`
- `IF` 可以匹配 `IF`
- `rb2410` 不会匹配 `RB`

也就是说，v1 暂不解析具体合约月份代码。

## 测试

```bash
python3 -m unittest discover -s tests
```

## 数据说明

每条品种记录包含：

- 品种代码
- 中文品种名
- 交易所代码
- 交易所中文名
- 上市日期
- 数据来源更新时间
- 市场标记

后续可以在同一数据结构中扩展境外期货品种。
