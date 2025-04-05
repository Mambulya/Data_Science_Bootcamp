#!/usr/bin/env python3
from financial import parse_website, get_request, parse_row_name
import pytest
import requests
# If I ask for Total Revenue, do I get the total revenue for the given ticker?
# Is the type of the return a tuple?
# If I give an invalid ticker name, do I get an exception?

def  test_get_request():
    ticker0 = "MSFT"
    assert get_request(ticker0).status_code == 200

    ticker1 = "AAPL"
    assert get_request(ticker1).status_code == 200

    ticker2 = "TSLA"
    assert get_request(ticker2).status_code == 200

def test_tuple():
    ticker0, field0 = "MSFT", "Tax Effect of Unusual Items"
    page_to_parse = get_request(ticker0)
    parse_website(page_to_parse, field0)
    assert type(parse_website(page_to_parse, field0)) is tuple

    ticker0, field0 = "AAPL", "Diluted EPS"
    page_to_parse = get_request(ticker0)
    parse_website(page_to_parse, field0)
    assert type(parse_website(page_to_parse, field0)) is tuple

    ticker0, field0 = "F", "Interest Income"
    page_to_parse = get_request(ticker0)
    parse_website(page_to_parse, field0)
    assert type(parse_website(page_to_parse, field0)) is tuple

def test_exception_0():
    with pytest.raises(Exception):
        page_to_parse = get_request("KGSDfsGsb")
        res_row = parse_website(page_to_parse, "Total Revenue")

def test_exception_1():
    with pytest.raises(Exception):
        page_to_parse = get_request("MSFT")
        res_row = parse_website(page_to_parse, "bebebbe")

def test_exception_2():
    with pytest.raises(Exception):
        page_to_parse = get_request("sdfn,s")
        res_row = parse_website(page_to_parse, "sdgfsdg")

def test_total_0():
    ticker, field = 'CRWD', 'EBITDA'
    page_to_parse = get_request(ticker)
    assert parse_website(page_to_parse, field) == ("EBITDA", "394,501.00", "293,827.00", "-40,754.00",
                                                   "-65,982.00", "-46,152.00")

def test_total_1():
    ticker, field = 'ORCL', 'Basic EPS'
    page_to_parse = get_request(ticker)
    assert parse_website(page_to_parse, field) == ("Basic EPS", "4.21", "3.82", "3.15", "2.49", "4.67")

def test_total_2():
    ticker, field = 'FTNT', 'Tax Effect of Unusual Items'
    page_to_parse = get_request(ticker)
    assert parse_website(page_to_parse, field) == ("Tax Effect of Unusual Items", "16,749.54", "--", "--", "--", "--")

if __name__ == "__main__":
    test_exception_0()
    print("+    test_exception0 has been successfully passed!")
    test_exception_1()
    print("+    test_exception1 has been successfully passed!")
    test_exception_2()
    print("+    test_exception2 has been successfully passed!")
    test_tuple()
    print("+    test_tuple has been successfully passed!")
    test_get_request()
    print("+    test_get_request has been successfully passed!")
    test_total_0()
    print("+    test_total_0 has been successfully passed!  ticker, field = 'CRWD', 'EBITDA'")
    test_total_1()
    print("+    test_total_1 has been successfully passed!  ticker, field = 'ORCL', 'Basic EPS'")
    test_total_2()
    print("+    test_total_2 has been successfully passed!  ticker, field = 'FTNT', 'Tax Effect of Unusual Items'")