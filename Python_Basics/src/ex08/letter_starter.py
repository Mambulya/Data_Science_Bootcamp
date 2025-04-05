"""
Create another script that takes an email, searches the corresponding name from the file created by the first script and returns the first paragraph of a letter:
Dear Ivan, welcome to our team. We are sure that it will be a pleasure to work with you. That’s a precondition for the professionals that our company hires.
"""

import sys

def get_name_from_file(path:str, email:str) -> str:
    res_name = ""
    with open(path, 'r') as f:
        for person in f.readlines()[1:]:
            if person.split('\t')[2][:-1] == email:
                return person.split('\t')[0]

def print_paragraph(name:str):
    print(f"Dear {name}, welcome to our team. We are sure that it will be a pleasure to work with you. That’s a precondition for the professionals that our company hires.\n")

if __name__ == "__main__":
    arguments = sys.argv[1:]
    if (len(arguments) == 1):
        email = arguments[0]
        name = get_name_from_file("employees.tsv", email)
        print_paragraph(name)