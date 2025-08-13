def main():
    time_str = input("What time is it? ").strip()

    time = convert(time_str)

    if time == -1:
        print("Not a valid time")
    else:
        if 7 <= time <= 8:
            print("breakfast time")
        elif 12 <= time <= 13:
            print("lunch time")
        elif 18 <= time <= 19:
            print("dinner time")

def convert(time):
    if ":" not in time: return -1

    if time.count(":") > 1: return -1

    hours, minutes = time.split(":")

    if hours == "": return -1
    if minutes == "": return -1

    for n in range(0,len(hours)):
        if hours[n] not in "0123456789": return -1
    for n in range(0,len(minutes)):
        if minutes[n] not in "0123456789": return -1

    hours = float(hours)
    minutes = float(minutes)

    flag = False
    for x in range(1,25):
        if hours == x:
            flag = True
            break
    if not flag: return -1

    flag = False
    for x in range(0,61):
        if minutes == x:
            flag = True
            break
    if not flag: return -1

    minutes = minutes / 60

    return hours + minutes

if __name__ == "__main__":
    main()
