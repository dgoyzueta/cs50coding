# Program: playback
def get_input_from_user():
    text = input("Enter text or phrase to play back: ")
    return text

def main():
    print(get_input_from_user().replace(" ", "..."))

main()
