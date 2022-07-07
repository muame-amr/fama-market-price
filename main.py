import re
from bs4 import BeautifulSoup
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from utils.utils import get_centres, get_data


def main():
    service = Service(executable_path=ChromeDriverManager().install())
    op = webdriver.ChromeOptions()
    op.add_argument("headless")
    driver = webdriver.Chrome(service=service, options=op)

    market_regex = r"(Farm|Wholesale|Retail)\sPrice"
    date_regex = r"[\d]{2}\s[A-Z]+\s[\d]{4}"

    base_URL = "https://www.fama.gov.my/en/harga-pasaran-terkini"

    driver.get(base_URL)
    main_soup = BeautifulSoup(driver.page_source, "html.parser")

    market_price_type = dict()
    market_type_tag = main_soup.find_all("a", string=re.compile(market_regex))

    for market_type in market_type_tag:
        market_price_type[market_type.text] = market_type.get("href")

    data = list()

    for market in market_price_type:

        print(f"Scraping {market}")

        driver.get(market_price_type[market])
        soup = BeautifulSoup(driver.page_source, "html.parser")

        # Get date uploaded
        date = re.search(date_regex, soup.find("h3").text).group(0)

        # Get centers list
        centres = get_centres(soup)

        # Get data
        data = data + get_data(soup, centres, market)

    # Get the centre
    df = pd.DataFrame(
        data,
        columns=[
            "Market Price Type",
            "Centre",
            "Variety Name",
            "Grade",
            "Unit",
            "Max Price",
            "Average Price",
            "Min. Price",
        ],
    )

    formatted_date = "_".join(date.lower().split(" "))
    df.to_csv("public/{}_market_price.csv".format(formatted_date), index=False)


if __name__ == "__main__":
    main()
