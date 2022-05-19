# Fama Market Price

Junior data engineer challenge to scrape latest market price from official portal of Federal Agricutural Marketing Authority (FAMA).

## Description

Scrape latest farm, wholesale and retail market prices from FAMA website. The prices are then combined together into a single table. The table shall be exported to a `.csv` file. The `.csv` file will have the following columns:

- `Market price type`: Farm, Wholesale or Retail
- `Centre`: Name of the centre
- `Variety Name`: Name of the variety
- `Grade`: Grade of the variety
- `Unit`: Unit of the variety
- `Max Price`: Maximum price of the variety
- `Average Price`: Average price of the variety
- `Min. Price`: Minimum price of the variety

## Getting Started

### Dependencies

- [Python 3](https://www.python.org/downloads/)
- [pip](https://pypi.org/project/pip/)
- [Git](https://git-scm.com/)

### Installing

**Clone this repository:**

```bash
git clone https://github.com/muame-amr/fama-market-price
cd fama-market-price

```

**Create a new virual environment:**

Conda

```bash
conda create -n <env_name> python=3.9
conda activate <env_name>
```

Virtualenv

```bash
python3 -m venv <env_name>
source <env_name>/bin/activate
```

**Install all the requirements:**

```bash
pip install -r requirements.txt
```

### Executing program

Run `script.py` to execute the program:

```bash
python script.py
```

`<date>_market_price.csv` file will be created in the public folder.

## License

This project is licensed under the MIT License - see the [LICENSE.md](https://github.com/muame-amr/fama-market-price/blob/main/LICENSE) file for details
