import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))

def bytes_ok(groups):
    if 0 <= int(groups[0]) <= 255 and 0 <= int(groups[1]) <= 255 \
           and 0 <= int(groups[2]) <= 255 and 0 <= int(groups[3]) <= 255:
        return True
    else:
        return False

def validate(ip):
    matches = re.search(r"^([0-9]{1,3})\.([0-9]{1,3})\.([0-9]{1,3})\.([0-9]{1,3})$", ip.strip())
    if matches:
        if bytes_ok(matches.groups()):
            return True
        else:
            return False
    else:
        return False

if __name__ == "__main__":
    main()
