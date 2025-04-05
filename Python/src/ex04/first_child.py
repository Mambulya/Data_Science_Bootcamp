import sys
import random
class Research:
    def __init__(self, path):
        self.file = path
    def file_reader(self, has_header=True):
        with open(self.file, "r") as f:
            lines = f.readlines()
            lines_to_print = []
            if not(lines[0].count('0') != 1 or lines[0].count('1') != 1 or lines[0].count(',') == 1):
                has_header = False
            for line in (lines[has_header:]):
                if not((line == "0,1\n") or (line == "1,0\n") or (line == "1,0") or (line == "1,0")):
                    raise ValueError("Not right input in file, should contain: \"0,1\" or \"1,0\"")
                lines_to_print.append([ int(line[0]) , int(line[2]) ])
        return lines_to_print

class Calculations:
    def __init__(self, data):
        self.contest = data
    def counts(self):
        heads = 0
        tails = 0
        for heads_tails in self.contest:
            heads += heads_tails[0]
            tails += heads_tails[1]
        return (heads, tails)
    @staticmethod
    def fractions(heads, tails):
        total = heads + tails
        return heads/total, tails/total

class Analitics(Calculations):
    @staticmethod
    def predict_random(predictions_num):
        predictions = []
        for _ in range(predictions_num):
            head = random.randint(0,1)
            tail = 1 - head
            predictions.append([head, tail])
        return predictions
    def predict_last(self):
        return self.contest[-1]


if __name__ == "__main__":
    if len(sys.argv) == 2:
        my_ins = Research(sys.argv[1])
        contest = my_ins.file_reader()
        # the data from file_reader()
        for line in contest:
            print(line, end=" ")
        # the counts from counts()
        c_ins = Calculations(contest)
        heads, tails = c_ins.counts()
        print(f"\n{heads} {tails}")
        # the fractions from fractions()
        freq_h, freq_t = Calculations.fractions(heads, tails)
        print(f"{freq_h} {freq_t}")
        # the list of lists from predict_random() for the 3 steps
        print(Analitics.predict_random(3))
        # the list from predict_last()
        a_ins = Analitics(contest)
        print(a_ins.predict_last())