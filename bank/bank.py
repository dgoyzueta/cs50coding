# Program: bank.py

def main():
    greeting = input("Enter greeting from the bank teller: ").strip()

    if "hello" in greeting.lower():
        print("$0")
    elif "h" == greeting.lower()[0]:
        print("$20")
    else:
        print("$100")

main()
