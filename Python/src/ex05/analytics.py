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
        return heads/total * 100, tails/total * 100

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
    @staticmethod
    def save_file(data, name_of_file, extension="txt"):
        if extension != "txt": raise ValueError("only txt format!")
        with open(f"{name_of_file}.{extension}", 'w') as f:
            f.write(data)
