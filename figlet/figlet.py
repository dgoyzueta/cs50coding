from pyfiglet import Figlet
from random import choice
import sys

def main():
    figlet = Figlet()
    fonts = figlet.getFonts()

    if len(sys.argv) == 3:
        if sys.argv[1] not in ["-f", "--font"]:
            sys.exit("Incorrect first argument: Not -f or --font")
        if sys.argv[2] not in fonts:
            sys.exit("Incorrect second argument: Font is not recognized.")
    elif len(sys.argv) == 2 or len(sys.argv) > 3:
        sys.exit("Fail to enter 2 arguments only.")

    text = input("Input: ").strip()

    if len(sys.argv) == 1:
        random_font = choice(fonts)
        figlet.setFont(font = random_font)
        print(figlet.renderText(text))
    else:
        figlet.setFont(font = sys.argv[2])
        print(figlet.renderText(text))

main()
