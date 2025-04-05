#!/usr/bin/env python3
import sys
import psutil

def generate_file(path:str) -> list:
    with open(path, "r") as f:
        for row in f:
            yield row

if __name__ == "__main__":
    arg = sys.argv
    if len(arg) == 2:
        path = arg[1]
        my_generator = generate_file(path)
        for _ in my_generator:
            pass

        ps = psutil.Process()
        print(f'Peak memory usage= {ps.memory_info().rss / (1024*1024*1024)} GB')   # переход из байтов в ГБ
        print(f'User Mode Time + System Mode Time = {ps.cpu_times().user + ps.cpu_times().system}s')