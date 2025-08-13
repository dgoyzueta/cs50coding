import re

def main():
    pattern = r'^\d{1,16}$'

    while True:
        cc = input("Enter credit card number: ").strip()
        if re.search(pattern, cc):
            break

    if valid_cc_number(cc):
        print(get_cc_type(cc))
    else:
        print("INVALID")


def valid_cc_number(cc):
    sum = 0
    for digit in cc[-2::-2]:
        temp = int(digit) * 2
        if temp >= 10:
            sum = sum + (temp // 10) + (temp % 10)
        else:
            sum = sum + temp

    for digit in cc[::-2]:
        sum = sum + int(digit)

    if sum % 10 == 0:
        return True
    else:
        return False


def get_cc_type(cc):
    if cc[0:2] in ["34", "37"] and len(cc) == 15:
        return "AMEX"
    if 51 <= int(cc[0:2]) <= 55 and len(cc) == 16:
        return "MASTERCARD"
    if cc[0:1] == "4" and (len(cc) in (13,16)):
        return "VISA"

    return "INVALID"


if __name__ == "__main__":
    main()
