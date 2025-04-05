import sys
import os
class Reasearch:
    def __init__(self, path):
        self.file = path
    def file_reader(self):
        if not os.path.exists(self.file):
            raise Exception("No such file! Try another path :)")
        with open(self.file, "r") as f:
            lines = f.readlines()
            if lines[0].count(',') != 1:
                raise ValueError("Not right header")
            for line in (lines[1:]):
                if not((line == "0,1\n") or (line == "1,0\n") or (line == "1,0") or (lines == "1,0")):
                    raise ValueError("Not right input in file, should contain: \"0,1\" or \"1,0\"")
        return lines

if __name__ == "__main__":
    if len(sys.argv) == 2:
        my_ins = Reasearch(sys.argv[1])
        for l in my_ins.file_reader():
            print(l, end="")
