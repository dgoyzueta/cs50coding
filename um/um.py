import re

def main():
    print(count(input("Text: ")))

def count(s):
    pattern = r"(?<![a-zA-Z])um(?![a-zA-Z])"
    lista = re.findall(pattern, s, re.IGNORECASE)
    return len(lista)

if __name__ == "__main__":
    main()
