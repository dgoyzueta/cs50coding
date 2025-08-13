import inflect
import sys

def main():
    p = inflect.engine()

    list_of_names = []

    while True:
        try:
            name = input("Name :").strip()
        except EOFError:
            print("\n")
            if list_of_names != []:
                print("Adieu, adieu, to", p.join(list_of_names))
            sys.exit()
        else:
            list_of_names.append(name)

main()
