# Program: camel.py
# Purpose: To convert a camel-case text into a snake-case text

def get_list_of_words_from_camel_case(camel):

    words = []
    upper_positions = []
    for i in range(len(camel)):
        if camel[i] in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            upper_positions.append(i)

    if upper_positions == []:
        words.append(camel)
        return words

    beginning = 0
    for n in upper_positions:
        words.append(camel[beginning:n])
        beginning = n
    words.append(camel[beginning:])

    return words


def convert_to_snake_case(words):

    snake_case = ""
    for w in words:
        snake_case = snake_case + w.lower() + "_"

    return snake_case[0:len(snake_case)-1]


def main():

    camel = input("Enter camel case text: ").strip()

    words = get_list_of_words_from_camel_case(camel)

    print(convert_to_snake_case(words))

main()
