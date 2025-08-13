import sys
import csv

def eval_arguments(argument):
    match len(argument):
        case 1:
            sys.exit("Too few command-line arguments")
        case 2:
            sys.exit("Too few command-line arguments")
        case 3:
            if argument[1][-4:] != ".csv":
                sys.exit("Not a CSV file")
            else:
                return True
        case _:
            sys.exit("Too many command-line arguments")

def main():

    if eval_arguments(sys.argv):
        output_dict = {}
        try:
            with open(sys.argv[1]) as file:
                reader = csv.DictReader(file)

                with open(sys.argv[2], "w") as csvfile:
                    writer = csv.DictWriter(csvfile, fieldnames = ['first', 'last', 'house'])
                    writer.writeheader()

                    for row in reader:
                        last, first = row["name"].split(",")
                        last = last.strip()
                        first = first.strip()
                        house = row["house"].strip()
                        output_dict = {'first': first, 'last':last, 'house': house}
                        writer.writerow(output_dict)

        except FileNotFoundError:
            sys.exit("File does not exist")

if __name__ == "__main__":
    main()
