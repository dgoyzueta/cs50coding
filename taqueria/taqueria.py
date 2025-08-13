def get_price(item):
    menu = {
        "Baja Taco": 4.25,
        "Burrito": 7.50,
        "Bowl": 8.50,
        "Nachos": 11.00,
        "Quesadilla": 8.50,
        "Super Burrito": 8.50,
        "Super Quesadilla": 9.50,
        "Taco": 3.00,
        "Tortilla Salad": 8.00
    }

    return menu.get(item.title())

def main():

    total = 0
    while True:
        try:
            item = input("Enter item: ").strip()
        except EOFError:
            print("\n")
            break
        else:
            price = get_price(item)
            if price != None:
                total = total + price
                print(f"Total: ${total:.2f}")
            else:
                print(f"Item: {item}")

main()
