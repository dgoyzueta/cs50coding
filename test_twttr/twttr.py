def shorten(word):
    vowels = "AEIOUaeiou"
    for v in vowels:
        word = word.replace(v,"")
    return word

def main():

    twitter = input("Input Twitter text: ")
    print(shorten(twitter))

if __name__ == "__main__":
    main()
