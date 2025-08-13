# Program: faces
def get_input_from_user():
    text = input("Enter text: ")
    return text

def convert(text):
    text = text.replace(":)","🙂")
    text = text.replace(":(","🙁")
    return text

def main():
    text = get_input_from_user()
    print(convert(text))

main()
