# Program deep.py

def main():
    answer = input("What is the Answer to the Greate Question of Life, the Universe, and Everything? ")

    match answer.strip().lower():
        case "forty-two" | "forty two" | "42":
            print("Yes")
        case _:
            print("No")

main()
