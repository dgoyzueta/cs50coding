def main():

    twitter = input("Input Twitter text: ")

    vowels = "AEIOUaeiou"

    for v in vowels:
        twitter = twitter.replace(v,"")

    print(twitter)

main()
