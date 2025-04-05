#!/usr/bin/env python3
from bs4 import BeautifulSoup
import sys
import time
import requests

def get_request(ticker_arg):
    headers = {'User-Agent': 'Mozilla/5.0'}
    url = f"https://finance.yahoo.com/quote/{ticker_arg.upper()}/financials/?p={ticker_arg.lower()}"
    page = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
    if page.status_code != 200:
        raise Exception("URL does not exist")
    return page

def parse_row_name(rows_list:list) -> list:
    """парсим 0 колонку с названиями строк, оставляем чисто название строчки"""
    res = []
    for name in rows_list:
        res.append(name.text)
    return res

def parse_website(page_arg, field_arg):
    soup = BeautifulSoup(page_arg.text, "html.parser")
    title = soup.title.string
    if title == "Symbol Lookup from Yahoo Finance":
        raise Exception("The ticker does not exist")
    odd_columns = soup.findAll('div', class_='column yf-t22klz alt')
    even_columns = soup.findAll('div', class_='column yf-t22klz')
    all_columns = []
    column_names = soup.findAll('div', class_='rowTitle yf-t22klz')

    # убираем теги
    odd_c = 0
    even_c = 0
    for line in range(len(column_names)):
        mini_row = []
        for i in range(1,6):
            if i % 2:
                mini_row.append(odd_columns[odd_c].text.strip())
                odd_c += 1
            else:
                mini_row.append(odd_columns[odd_c].text.strip())
                even_c += 1
        all_columns.append(mini_row)

    column_names = parse_row_name(column_names)

    del odd_columns
    del even_columns

    if field_arg not in column_names:
        raise Exception(f"The field '{field_arg}' is not found")
    else:
        index = column_names.index(field_arg)
        res = [field_arg] + all_columns[index]
        return tuple(res)


if __name__ == "__main__":
    arguments = sys.argv
    if len(arguments) == 3:
        ticker, field = arguments[1], arguments[2]
        page_to_parse = get_request(ticker)
        res_row = parse_website(page_to_parse, field)
        print(res_row)
