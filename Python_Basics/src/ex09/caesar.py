import sys

def encode(mes:str, shift:int) -> str:
    res = ""
    russian_letters = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
    for letter in mes:
        if letter.upper() in russian_letters:
            raise Exception("Only English letters, please!")
        if letter.isalpha():
            if letter.isupper():
                letter = chr((ord(letter) + shift - 65) % 26 + 65)
            else:
                letter = chr((ord(letter) + shift - 97) % 26 + 97)
        res += letter

    return res


def decode(mes:str, shift:int) -> str:
    res = ""
    for letter in mes:
        if letter.isalpha():
            if letter.isupper():
                letter = chr((ord(letter) + -shift - 65) % 26 + 65)
            else:
                letter = chr((ord(letter) + -shift - 97) % 26 + 97)
        res += letter
    return res
    

if __name__ == "__main__":
    arguments = sys.argv[1:]
    if len(arguments) == 3:
        operation, messege, shift = arguments
        if int(shift) < 0:
            raise Exception("Shift < 0")
        if operation == "encode" or operation == "decode":
            if operation == "encode":
                print(encode(messege, int(shift)))
            else:
                print(decode(messege, int(shift)))