import sys
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
        @staticmethod
        def counts(contest_arg):
            heads = 0
            tails = 0
            for heads_tails in contest_arg:
                heads += heads_tails[0]
                tails += heads_tails[1]
            return (heads, tails)
        @staticmethod
        def fractions(heads, tails):
            total = heads + tails
            return heads/total, tails/total

if __name__ == "__main__":
    if len(sys.argv) == 2:
        my_ins = Research(sys.argv[1])
        contest = my_ins.file_reader()

        for line in contest:
            print(line, end=" ")

        heads, tails = Research.Calculations.counts(contest)
        print(f"\n{heads} {tails}")

        freq_h, freq_t = Research.Calculations.fractions(heads, tails)
        print(f"{freq_h} {freq_t}")
