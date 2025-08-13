import re
import sys
import inflect
from datetime import date

def validate_date_format(d):
    pattern = r"([0-9]{4})-([0-9]{2})-([0-9]{2})"
    date_parts = re.search(pattern, d)
    if not date_parts:
        sys.exit("Invalid date")

    year = int(date_parts.group(1))
    month = int(date_parts.group(2))
    day = int(date_parts.group(3))

    try:
        birth = date(year, month, day)
    except ValueError:
        sys.exit("Invalid date")
    else:
        return d


def life_in_minutes(birthdate):
    dob = date.fromisoformat(birthdate)
    p = inflect.engine()
    total_days = abs(date.today() - dob)
    total_minutes = total_days.days * 24 * 60
    return (p.number_to_words(total_minutes).replace("and ","")+" minutes").capitalize()


def main():

    dob = input("Date of Birth: ").strip()

    birthdate = validate_date_format(dob)

    total_minutes_words = life_in_minutes(birthdate)

    print(total_minutes_words)


if __name__ == "__main__":
    main()
