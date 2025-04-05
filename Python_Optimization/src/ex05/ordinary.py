#!/usr/bin/env python3
import sys
import psutil

def read_file(path:str) -> list:
    with open(path, "r") as f:
        lines = f.readlines()
    return lines

if __name__ == "__main__":
    arg = sys.argv
    if len(arg) == 2:
        path = arg[1]
        lines = read_file(path)
        for _ in lines:
            pass

        ps = psutil.Process()
        print(f'Peak memory usage= {ps.memory_info().rss / (1024*1024*1024)} GB')
        print(f'User Mode Time + System Mode Time = {ps.cpu_times().user + ps.cpu_times().system}s')

# ./generator.py ratings.csv
# Peak memory usage= 0.012378692626953125 GB
# User Mode Time + System Mode Time = 0.088829865s

# Peak memory usage= 1.36456298828125 GB
# User Mode Time + System Mode Time = 0.105482824s