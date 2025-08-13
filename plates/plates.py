def main():
    plate = input("Plate: ").strip()
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):

    if len(s) < 2 or len(s) > 6:
        return False

    if s[0].upper() not in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or s[1].upper() not in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        return False

    for p in s:
        if p not in "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789":
            return False

    first_num = False
    for i in range(2,len(s)):
        if first_num == True and s[i] in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            return False
        if s[i] in "0123456789" and first_num == False:
            first_num = True
            if s[i] == "0":
                return False

    return True


main()
