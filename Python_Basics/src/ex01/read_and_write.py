"""
open the file ds.csv, read the data it contains, replace all the comma delimiters with ’\t’ 
and save it to another file ds.tsv. Be careful, your data may contain commas. 
If you replace them, you will corrupt the data.
"""

if __name__ == "__main__":
    new_F = open("new_ds.tsv", "w")

    with open("ds.csv") as F:
        for line in F.readlines():
            parts = line.split("\"")
            for i in range(1, len(parts)):
                if (parts[i] == ","):
                    parts[i] = "\t"
                if (i == 6):
                    parts[i] = parts[i].replace(",", "\t")
                new_F.write(parts[i])