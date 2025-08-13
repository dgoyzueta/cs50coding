def get_x_y(fraction):
    values = fraction.split("/")
    if len(values) != 2:
        return None,None
    try:
        x = int(values[0])
    except ValueError:
        return None,None
    else:
        try:
            y = int(values[1])
        except ValueError:
            return None,None
        else:
            if x <= y:
                return x,y
            else:
                return None,None

def get_tank_status(x,y):
    try:
        tank_status = x / y
    except ValueError:
        return None
    except ZeroDivisionError:
        return None
    else:
        tank_status = tank_status * 100
        if tank_status <= 1:
            return "E"
        elif tank_status >= 99:
            return "F"
        else:
            return str(int(round(tank_status,0)))+"%"

def main():
    while True:
        fraction = input("Enter fraction: ").strip()
        x,y = get_x_y(fraction)
        if x != None and y != None:
            tank_status = get_tank_status(x,y)
            if tank_status != None:
                print(tank_status)
                break
main()
