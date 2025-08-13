import re

def main():
    pattern = r'^\d+(\.\d{1,2})?$'

    while True:
        h = input("Change: ").strip()
        if re.search(pattern, h):
            break

    money = int(float(h) * 100)
    num_coins = get_num_coins(money)
    print(num_coins)


def get_num_coins(amount):
    quarters = amount // 25
    after_quarters = amount % 25
    dimes = 0
    after_dimes = 0
    nickels = 0
    after_nickels = 0

    if after_quarters > 0:
        dimes = after_quarters // 10
        after_dimes = after_quarters % 10

        nickels = 0
        if after_dimes > 0:
            nickels = after_dimes // 5
            after_nickels = after_dimes % 5

    return quarters + dimes + nickels + after_nickels


if __name__ == "__main__":
    main()
