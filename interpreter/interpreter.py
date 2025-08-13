# Program:interpreter.py
# Goal: To do simple arithmetic calculations between 2 integers
def find_op_position(expression):
    if "+" in expression: return expression.find("+")
    if "-" in expression: return expression.find("-")
    if "*" in expression: return expression.find("*")
    if "/" in expression: return expression.find("/")

    return -1

def main():
    print("Input your arithmetic operation between 2 integers X and Y. Use + - * / for operations")
    expression = input("Enter expression: ")

    op_pos = find_op_position(expression)
    if op_pos == -1:
        print("It is an invalid arithmetic operation")
        return

    op = expression[op_pos]
    x = expression[0:op_pos].strip()
    y = expression[op_pos+1:].strip()

    if x == "" or y == "":
        print("It is an invalid arithmetic operation")
        return

    x = int(x)
    y = int(y)

    match op:
        case "+":
            print(f"{(x+y):.1f}")
        case "-":
            print(f"{(x-y):.1f}")
        case "*":
            print(f"{(x*y):.1f}")
        case "/":
            if y == 0:
                print("Cannot divide by 0")
            else:
                print(f"{(x/y):.1f}")
        case _:
            print("Invalid arithmetic operator")

main()
