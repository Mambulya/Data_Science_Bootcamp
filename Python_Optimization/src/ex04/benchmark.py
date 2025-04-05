#!/usr/bin/env python3

import timeit
import sys
from collections import Counter
import random

def genereate_random_numbers(len_arg:int, start:int, end:int) -> list:
    """generate a list with 1 000 000 random values from 0 to 100 (remember list compre- hensions?)"""
    res = [random.randint(start, end) for _ in range(len_arg)]
    return res

def calculate_counts(src_list:list) -> dict:
    """write a function that creates a dict out of the list where the
    keys are the numbers from 0 to 100 and the values are their counts"""
    res_d = dict()
    for num in src_list:
        try:
            res_d[num] += 1
        except KeyError: # число встресается первый раз
            res_d[num] = 1
    return res_d


def get_top(src_list, top = 10) -> dict:
    """write a function that returns the top 10 most common numbers where the
    keys are the numbers and the values are the counts, the input is the list"""
    top_d = dict()
    counts = []
    for num in src_list:
        counts.append(src_list.count(num))
    for _ in range(top):
        index_max_count = counts.index(max(counts))
        top_d[src_list[index_max_count]] = max(counts)
        counts[index_max_count] = -1
    return top_d

def calculate_counts_counter(src_list:list) -> dict:
    """write a function that creates a dict out of the list where the
    keys are the numbers from 0 to 100 and the values are their counts"""
    res_dict = dict(Counter(src_list))
    return res_dict


def get_top_counter(src_list, top = 10) -> dict:
    """write a function that returns the top 10 most common numbers where the
    keys are the numbers and the values are the counts, the input is the list"""
    top = dict(Counter(src_list).most_common(top))
    return top

def calculate_counts_time(numbers:list, calls_arg=10000000) -> int:
    SETUP_CODE = """
from __main__ import calculate_counts
    """
    TEST_CODE = f"""
my_counts_d = calculate_counts({numbers})
    """
    TIME = timeit.timeit(setup=SETUP_CODE, stmt=TEST_CODE, number = calls_arg)
    return TIME


def calculate_counts_counter_time(numbers:list, calls_arg=10000000) -> int:
    SETUP_CODE = """
from __main__ import calculate_counts_counter
    """
    TEST_CODE = f"""
my_counts_d = calculate_counts_counter({numbers})
    """
    TIME = timeit.timeit(setup=SETUP_CODE, stmt=TEST_CODE, number = calls_arg)
    return TIME


def get_top_time(numbers:list, calls_arg=10000000) -> int:
    SETUP_CODE = """
from __main__ import get_top
    """
    TEST_CODE = f"""
my_top_d = get_top({numbers})
    """
    TIME = timeit.timeit(setup=SETUP_CODE, stmt=TEST_CODE, number = calls_arg)
    return TIME


def get_top_counter_time(numbers:list, calls_arg=10000000) -> int:
    SETUP_CODE = """
from __main__ import get_top_counter
    """
    TEST_CODE = f"""
my_top_d = get_top_counter({numbers})
    """
    TIME = timeit.timeit(setup=SETUP_CODE, stmt=TEST_CODE, number = calls_arg)
    return TIME


if __name__ == "__main__":
    numbers_l = genereate_random_numbers(10, 0, 10)

    # my_counts_d = calculate_counts(numbers_l)
    # my_top_ten = get_top(numbers_l, 10)
    #
    # counter_counts_d = calculate_counts_counter(numbers_l)
    # counter_top_ten = get_top_counter(numbers_l, 10)
    # # my results vs Counter results
    # print(my_counts_d)
    # print(counter_counts_d)
    #
    # print(my_top_ten)
    # print(counter_top_ten)

    print("=============== Task 2 =============")
    print(f"my function: {calculate_counts_time(numbers_l)}")
    print(f"Counter:      {calculate_counts_counter_time(numbers_l)}")

    print("=============== Task 3 =============")
    print(f"my function: {get_top_time(numbers_l)}")
    print(f"Counter:      {get_top_counter_time(numbers_l)}")

    # results
    # =============== Task 2 =============
    # my function: 17.799824792
    # Counter:      22.184411125
    # =============== Task 3 =============
    # my function: 99.145229917
    # Counter:      35.096962875
