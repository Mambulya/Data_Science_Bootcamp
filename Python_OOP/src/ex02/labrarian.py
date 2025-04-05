#!/usr/bin/env python3
# chmod +x venv.py
import sys
import os

def func(src_lib_file):
    if sys.prefix != sys.base_prefix: # the kamilahb env is running
        os.system(f"pip install -r {src_lib_file}")
        print("Libs were installed successfully!")
    else:
        raise Exception("not in the virtual environment!")

def print_installed_libs():
    os.system("pip freeze")
    os.system("pip freeze > requirements.txt")

if __name__ == "__main__":
    func("my_requirements.txt")
    print_installed_libs()