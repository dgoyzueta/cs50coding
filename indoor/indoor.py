def get_input_from_user():
    text = input("Enter text or phrase: ")
    return text

def main():
    print(get_input_from_user().lower())

main()
