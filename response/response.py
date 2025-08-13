from validator_collection import checkers

def email_check(email):
    if checkers.is_email(email):
        return "Valid"
    else:
        return "Invalid"

def main():
    email = input("Enter email address: ").strip()

    print(email_check(email))

if __name__ == "__main__":
    main()
