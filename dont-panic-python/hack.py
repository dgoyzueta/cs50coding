from cs50 import SQL

def main():
    db = SQL("sqlite:///dont-panic.db")

    while True:
        password = input("Enter password for the admin user:").strip()
        if password != "":
            break

    db.execute("update users set username = 'admin', password = ? where username = 'admin'", password)

if __name__ == "__main__":
    main()

