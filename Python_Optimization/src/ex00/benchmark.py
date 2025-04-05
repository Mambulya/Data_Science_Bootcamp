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

if __name__ == "__main__":
    res1 = lc_time()
    res2 = loop_time()
    if res1 <= res2:
        print(f"it is better to use a list comprehension\n{res1} vs ", end="")
        res_not_to_print = res2
    else:
        print(f"it is better to use a loop\n{res2} vs ", end="")
        res_to_print = res1
    print(res_not_to_print)


#it is better to use a list comprehension
#34.832479459 vs 37.88508075
