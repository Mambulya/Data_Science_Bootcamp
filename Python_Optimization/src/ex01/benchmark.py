#!/usr/bin/env python3
# chmod +x venv.py
import timeit


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

def lc_time() -> float:
    SETUP_CODE ="""
from __main__ import lc
    """
    TEST_CODE = """
emails = ["john@gmail.com", "james@gmail.com", "alice@yahoo.com", "anna@live.com", "philipp@gmail.com"] * 5
new_emails = lc(emails)
    """

    TIME = timeit.timeit(setup=SETUP_CODE, stmt=TEST_CODE, number=100000)
    return TIME


def loop_time() -> float:
    SETUP_CODE ="""
from __main__ import loop
    """
    TEST_CODE = """
emails = ["john@gmail.com", "james@gmail.com", "alice@yahoo.com", "anna@live.com", "philipp@gmail.com"] * 5
new_emails = loop(emails)
    """

    TIME = timeit.timeit(setup=SETUP_CODE, stmt=TEST_CODE, number=100000)
    return TIME


def my_map_time() -> float:
    SETUP_CODE = """
from __main__ import my_map
        """
    TEST_CODE = """
emails = ["john@gmail.com", "james@gmail.com", "alice@yahoo.com", "anna@live.com", "philipp@gmail.com"] * 5
new_emails = my_map(emails)
        """

    TIME = timeit.timeit(setup=SETUP_CODE, stmt=TEST_CODE, number=100000)
    return TIME

if __name__ == "__main__":
    res1 = lc_time()
    res2 = loop_time()
    res3 = my_map_time()

    results = {res1 : "it is better to use a list comprehension",
               res2 : "it is better to use a loop",
               res3 : "it is better to use a map"
    }

    sorted_res = sorted(results.keys())
    for i in range(len(sorted_res)):
        if i == 0:  # the fastest construction
            print(results[sorted_res[i]])
        if i == len(sorted_res) - 1:
            print(sorted_res[i])
        else:
            print(f"{sorted_res[i]} vs ", end="")

# it is better to use a map (without list())
# 3.3656748339999893 vs 35.302425209 vs 38.379564040999995

# it is better to use a list comprehension
# 36.044325709000006 vs 39.328259542000005 vs 45.165943959