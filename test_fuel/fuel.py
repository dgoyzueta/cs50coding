def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return str(percentage)+"%"

def convert(fraction):
    values = fraction.split("/")

    if len(values) != 2:
        raise ValueError("Input is not in the form N/M where N and M are integers.")

    try:
        x = int(values[0])
        y = int(values[1])
    except ValueError:
        raise ValueError("X and Y must be integers.")

    if y == 0:
        raise ZeroDivisionError("Error because of division by 0.")

    if x > y:
        raise ValueError("Numerator is greater that denominator.")

    tank_status = round((x / y) * 100)

    if tank_status < 0 or tank_status > 100:
        raise ValueError("Percentage must be between 0 and 100 inclusive.")

    return tank_status


def main():
    while True:
        fraction = input("Enter fraction: ").strip()
        fraction_integer = convert(fraction)
        if fraction_integer != -1:
            print(gauge(fraction_integer))
            break

if __name__ == "__main__":
    main()
