import sys
import csv
from tabulate import tabulate

def eval_arguments(argument):
    match len(argument):
        case 1:
            sys.exit("Too few command-line arguments")
        case 2:
            if argument[1][-4:] != ".csv":
                sys.exit("Not a CSV file")
            else:
                return True
        case _:
            sys.exit("Too many command-line arguments")

def main():

    if eval_arguments(sys.argv):
        count = 0
        try:
            with open(sys.argv[1]) as file:
                reader = csv.DictReader(file)
                print(tabulate(reader, headers="keys", tablefmt="grid"))

        except FileNotFoundError:
            sys.exit("File does not exist")

if __name__ == "__main__":
    main()
