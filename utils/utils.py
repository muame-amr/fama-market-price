from bs4 import BeautifulSoup


def get_centres(soup: BeautifulSoup) -> list:
    """
    Get the list of name of fama market centres.

    Args:
        soup: BeautifulSoup object containing parsed HTML.

    Returns:
        The list of market centres.
    """
    centres = list()
    for b_element in soup.find_all("b"):
        if b_element.text not in ["[", "]"]:
            centre_name = " ".join(b_element.text.split(" ")[-3:]).strip(" :")
            centres.append(centre_name)
    return centres


def get_data(soup: BeautifulSoup, centres: list, market: str) -> list:
    """
    Get the variety data of particular market.

    Args:
        soup: BeautifulSoup object containing parsed HTML.
        centres: The list of market centres.
        market: The market name.

    Returns:
        The list of data rows.
    """
    rows = list()
    data_tables = soup.find_all("table")[0].find_all("table")[1::2]
    for tables, centre in zip(data_tables, centres):
        for tr_element in tables.find_all("tr")[2:]:
            td_elements = tr_element.find_all("td")
            # variety_id = tr_element['id']
            variety_name = td_elements[0].text
            grade = td_elements[1].text
            unit = td_elements[2].text.replace("KILOGRAM", "KG")
            max_price = "%.2f" % float(td_elements[3].text)
            avg_price = "%.2f" % float(td_elements[4].text)
            min_price = "%.2f" % float(td_elements[5].text)
            rows.append(
                [
                    market,
                    centre,
                    variety_name,
                    grade,
                    unit,
                    max_price,
                    avg_price,
                    min_price,
                ]
            )
    return rows
