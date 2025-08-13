import re
import sys


def main():
    print(convert(input("Hours: ")))

def convert_24(schedule):
    hour01 = int(schedule[0])
    if schedule[2] == "PM":
        if hour01 < 12:
            hour01 = hour01 + 12

    if hour01 == 12 and schedule[2] == "AM":
        hour01 = 0

    hour02 = int(schedule[3])
    if schedule[5] == "PM":
        if hour02 < 12:
            hour02 = hour02 + 12

    if hour02 == 12 and schedule[5] == "AM":
        hour02 = 0

    if not schedule[1]:
        minute01 = "00"
    else:
        minute01 = schedule[1]
        minute01 = minute01[1:]

    if not schedule[4]:
        minute02 = "00"
    else:
        minute02 = schedule[4]
        minute02 = minute02[1:]

    if not (00 <= int(minute01) <= 59):
        raise ValueError("Minutes from first hour not in range 00 to 59")

    if not (00 <= int(minute02) <= 59):
        raise ValueError("Minutes from second hour not in range 00 to 59")

    hour01 = str(hour01)
    hour02 = str(hour02)
    if hour01 in ["0","1","2","3","4","5","6","7","8","9"]:
        hour01 = "0"+hour01
    if hour02 in ["0","1","2","3","4","5","6","7","8","9"]:
        hour02 = "0"+hour02

    return hour01+":"+minute01+" to "+hour02+":"+minute02

def convert(s):
    m = re.search(r"^([0-9]{1,2})(:[0-9]{2})? (AM|PM) to ([0-9]{1,2})(:[0-9]{2})? (AM|PM)$",s.strip())
    if m:
        working_24 = convert_24(m.groups())
        return working_24
    else:
        raise ValueError("Not correct format for schedule")


if __name__ == "__main__":
    main()
