def main():

    due = 50
    paid = 0
    while True:

        print(f"Amount Due: {due}")
        coin = int(input("Insert Coin: "))

        if coin in [25,10,5]:
            paid += coin
            due = due - coin

            if paid >= 50:
               break

    print(f"Change Owed: {paid - 50}")

main()

