# Program: bank.py

def main():
    greeting = input("Enter greeting from the bank teller: ").strip()
    print(value(greeting))

def value(greeting):
    if "hello" == greeting[0:5].lower():
        return 0
    elif "h" == greeting[0].lower() and "hello" != greeting[0:5].lower():
        return 20
    else:
        return 100

if __name__ == "__main__":
    main()
