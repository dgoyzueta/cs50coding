import sys

def eval_arguments(argument):
    match len(argument):
        case 1:
            sys.exit("Too few command-line arguments")
        case 2:
            if argument[1][-3:] != ".py":
                sys.exit("Not a python file")
            else:
                return True
        case _:
            sys.exit("Too many command-line arguments")

def main():

    if eval_arguments(sys.argv):
        count = 0
        try:
            with open(sys.argv[1], "r") as file:
                lines = file.readlines()
        except FileNotFoundError:
            sys.exit("File does not exist")
        else:
            for line in lines:
                if not (line.strip().startswith("#") or line.strip() == ""):
                    count = count + 1
            print(count)

if __name__ == "__main__":
    main()
