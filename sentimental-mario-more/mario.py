import re

def main():
    pattern = r'^(?:[1-9].*)$'

    while True:
        h = input("Height: ").strip()
        if re.search(pattern, h):
            h = int(h)
            if h < 9:
                break


    for line in range(1, h+1):
        print(" " * (h-line), end = "")
        print("#" * line, end = "")
        print("  ", end = "")
        print("#" * line)

if __name__ == "__main__":
    main()
