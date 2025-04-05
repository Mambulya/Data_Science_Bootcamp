class Research:
    def file_reader(self):
        contest = ""
        with open("../ex00/data.csv", "r") as f:
            contest = f.read()
        return contest

if __name__ == "__main__":
    my_ins = Research()
    print(my_ins.file_reader())