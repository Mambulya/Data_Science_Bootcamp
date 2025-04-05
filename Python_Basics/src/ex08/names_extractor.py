import sys

def read_accounts(path:str) -> list:
    with open(path, 'r') as f:
        accounts = f.readlines()
    return accounts
        
def complete_file(path:str, accounts:list):
    with open(path, 'w') as f:
        f.write("Name\tSurname\tE-mail\n")
        for email in accounts:
            name, surname, _ = email.split('.')
            surname = surname.split('@')[0]
            f.write(f"{name.capitalize()}\t{surname.capitalize()}\t{email}")
        f.write("\n")



if __name__ == "__main__":
    argument = sys.argv[1:]
    if (len(argument) == 1):
        accounts = read_accounts(argument[0])
        open("employees.tsv", 'w')
        complete_file("employees.tsv", accounts)