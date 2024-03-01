import os.path
import sys

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

if __name__ == '__main__':
    from converter import toLetters

    print("Number To Letters Converter")
    while True:
        value = input('Number: ')
        if value.isdigit():
            print(toLetters(value))
        else:
            print("Enter only digits !!!")
