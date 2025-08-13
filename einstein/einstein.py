# Program: einstein.py
def valid_input(kg):
    for pos in range(0, len(kg)):
        if kg[pos] not in "0123456789":
            return False
        return True

def main():
    kg = input("Input mass in Kilograms: ").strip()
    if valid_input(kg):
        print(round(int(kg) * 90000000000000000))
    else:
        print("Incorrect input. This is not a integer number.")

main()
