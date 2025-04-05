#!/usr/bin/env python3

import timeit
import sys
from functools import reduce

def calculate_sum_loop(n:int) -> int:
    sum = 0
    for i in range(1, n+1):
        sum += i*i
    return sum


def reduce_sum(n:int) -> int:
    arr = list(range(1, n+1))
    res = reduce(lambda x, y: x + y*y, arr)
    return res


def calculate_sum_loop_time(n:int, calls_arg:int) -> int:
    SETUP_CODE = """
from __main__ import calculate_sum_loop
    """
    TEST_CODE = f"""
res = calculate_sum_loop({n})
    """
    TIME = timeit.timeit(setup=SETUP_CODE, stmt=SETUP_CODE, number = calls_arg)
    return TIME


def reduce_sum_time(n:int, calls_arg:int) -> int:
    SETUP_CODE = """
from __main__ import reduce_sum
    """
    TEST_CODE = f"""
res = reduce_sum({n})
    """
    TIME = timeit.timeit(setup=SETUP_CODE, stmt=TEST_CODE, number = calls_arg)
    return TIME


if __name__ == "__main__":
    arg = sys.argv
    if len(arg) == 4:
        func = arg[1]

        try:
            calls = int(arg[2])
            num = int(arg[3])
        except ValueError:
            raise ValueError(f"Not correct type of calls or num: {type(calls)}, {type(num)}")

        if func != "loop" and func != "reduce":
            raise ValueError("Not correct function (only 'loop' or 'reduce')")

        if func == "loop":
            print(calculate_sum_loop_time(num, calls))
        elif func == "reduce":
            print(reduce_sum_time(num, calls))
        else:
            print("Not correct function")

# ./benchmark.py loop 10000000 5
# 8.245086083
# ./benchmark.py reduce 10000000 5
# 8.538053875000001

# ./benchmark.py reduce 1000 5
# 0.0009084170000000016
# ./benchmark.py loop 1000 5
# 0.0010192080000000006

# ./benchmark.py reduce 1000 10000
# 1.179845583
# ./benchmark.py loop 1000 10000
# 0.0008458749999999959

# ./benchmark.py reduce 1000000 100
# 10.538395708
# ./benchmark.py loop 1000000 100
# 0.80514375




"""
                            много вызовов
         loop                     |             loop
                                  |  
маленькие числа ------------------|------------------------ большие числа 
                                  |  
        reduce                    |             loop
                            мало вызовов
"""