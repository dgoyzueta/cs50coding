def get_month(month_text):
    months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
    ]
    return months.index(month_text)

def get_elements_date(xdate):
    dd = ""
    mm = ""
    yyyy = ""

    if "," in xdate:
        try:
            elements = xdate.split(" ")
            if len(elements) == 3:
                if "," in elements[1]:
                    mm = get_month(elements[0].capitalize())
                    dd = elements[1].replace(",","")
                    yyyy = elements[2]

                    if int(dd) < 1 or int(dd) > 31:
                        return None

                    mm = mm + 1
                    mm = str(mm)
                    if len(mm) == 1:
                        mm = "0" + str(mm)

                    if len(dd) == 1:
                        dd = "0"+ dd

                    return yyyy+"-"+mm+"-"+dd
        except ValueError:
            return None

    if xdate.count("/") == 2:
        try:
            elements = xdate.split("/")

            if len(elements) == 3:
                dd = elements[1]
                mm = elements[0]
                yyyy = elements[2]

                if int(dd) < 1 or int(dd) > 31:
                    return None
                if len(dd) == 1:
                    dd = "0"+ dd
                if int(mm) < 1 or int(mm) > 12:
                    return None
                if len(mm) == 1:
                    mm = "0" + str(mm)

                return yyyy+"-"+mm+"-"+dd
        except ValueError:
            return None

    return None


def main():
    while True:
        try:
            input_date = input("Date: ").strip()

            converted_date = get_elements_date(input_date)

            if converted_date != None:
                print(converted_date)
                break

        except EOFError:
            break
        except ValueError:
            continue

main()
