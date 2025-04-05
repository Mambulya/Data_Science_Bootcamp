#!/usr/bin/env python3
# chmod +x venv.py
import timeit
import sys

def lc(src_emails:list) -> list:
    """list comprehension"""
    res = [email for email in src_emails if email.endswith("@gmail.com")]
    return res


def loop(src_emails:list) -> list:
    """loop"""
    res = []
    for email in src_emails:
        if email.endswith("@gmail.com"):
            res.append(email)
    return res


def my_map(src_emails:list) -> list:
    """map"""
    res = list(map(lambda x: x if x.endswith("@gmail.com") else None, src_emails))
    return res

def my_filter(src_emails:list) -> list:
    """filter"""
    res = list(filter(lambda x: x.endswith("@gmail.com"), src_emails))
    return res

def lc_time(calls:int) -> float:
    SETUP_CODE ="""
from __main__ import lc
    """
    TEST_CODE = """
emails = ["john@gmail.com", "james@gmail.com", "alice@yahoo.com", "anna@live.com", "philipp@gmail.com"] * 5
new_emails = lc(emails)
    """

    TIME = timeit.timeit(setup=SETUP_CODE, stmt=TEST_CODE, number=calls)
    return TIME


def loop_time(calls:int) -> float:
    SETUP_CODE ="""
from __main__ import loop
    """
    TEST_CODE = """
emails = ["john@gmail.com", "james@gmail.com", "alice@yahoo.com", "anna@live.com", "philipp@gmail.com"] * 5
new_emails = loop(emails)
    """

    TIME = timeit.timeit(setup=SETUP_CODE, stmt=TEST_CODE, number=calls)
    return TIME


def my_map_time(calls:int) -> float:
    SETUP_CODE = """
from __main__ import my_map
        """
    TEST_CODE = """
emails = ["john@gmail.com", "james@gmail.com", "alice@yahoo.com", "anna@live.com", "philipp@gmail.com"] * 5
new_emails = my_map(emails)
        """

    TIME = timeit.timeit(setup=SETUP_CODE, stmt=TEST_CODE, number=calls)
    return TIME

def my_filter_time(calls:int) -> float:
    SETUP_CODE = """
from __main__ import my_filter
        """
    TEST_CODE = """
emails = ["john@gmail.com", "james@gmail.com", "alice@yahoo.com", "anna@live.com", "philipp@gmail.com"] * 5
new_emails = my_filter(emails)
        """

    TIME = timeit.timeit(setup=SETUP_CODE, stmt=TEST_CODE, number=calls)
    return TIME

if __name__ == "__main__":
    arguments = sys.argv
    if len(arguments) == 3:
        function = arguments[1]
        calls_num = int(arguments[2])

        if calls_num <= 0:
            raise ValueError("Not correct number of calls: <= 0")

        if function == "list_comprehension":
            res = lc_time(calls_num)
        elif function == "loop":
            res = loop_time(calls_num)
        elif function == "map":
            res = my_map_time(calls_num)
        elif function == "filter":
            res = my_filter_time(calls_num)
        else:
            raise ValueError("Not correct function: (loop, list comprehension, map, filter)")

        print(res)

# ./benchmark.py filter 9000000
# 44.714142375
