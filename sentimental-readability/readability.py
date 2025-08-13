import re

def main():
    text = input("Enter text to evaluate US reading level: ").strip()

    num_letters = get_num_letters(text)
    num_words = get_num_words(text)
    num_sentences = get_num_sentences(text)
    print_reading_level(num_letters, num_words, num_sentences)

def get_num_letters(text):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    num = 0
    for letter in text:
        if letter.upper() in alphabet:
            num = num + 1
    return num

def get_num_words(text):
    return len(text.split())

def get_num_sentences(text):
    sentences = re.split(r"(?<=[.!?]) +", text)
    return len(sentences)

def print_reading_level(num_letters, num_words, num_sentences):
    index = 0.0588 * ((num_letters/num_words)*100) - 0.296 * ((num_sentences/num_words)*100) - 15.8

    if index < 1:
        print("Before Grade 1")
    elif index  > 16:
        print("Grade 16+")
    else:
        print(f"Grade {int(round(index))}")


if __name__ == "__main__":
    main()
