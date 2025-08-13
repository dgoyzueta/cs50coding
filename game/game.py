from random import randint
import sys

def main():

    while True:
        level = input("Level: ").strip()

        if level.isdigit():

            if int(level) != 0:

                random_number = randint(1, int(level))

                while True:
                    guess = input("Guess: ").strip()

                    if guess.isdigit():

                        if int(guess) > random_number:
                            print("Too large!")
                        elif int(guess) < random_number:
                            print("Too small!")
                        else:
                            print("Just right!")
                            sys.exit()

main()
