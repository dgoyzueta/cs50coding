import sys
from PIL import Image, ImageOps

def crop_to_square(image):
    width, height = image.size
    min_side = min(width, height)
    left = (width - min_side) / 2
    top = (height - min_side) / 2
    right = (width + min_side) / 2
    bottom = (height + min_side) / 2

    return image.crop((left, top, right, bottom))

def compare_extensions(input_file, output_file):
    input_ext = input_file[input_file.rfind("."):]
    output_ext = output_file[output_file.rfind("."):]

    if input_ext.lower() == output_ext.lower():
        return True
    else:
        return False

def eval_arguments(argument):
    match len(argument):
        case 1:
            sys.exit("Too few command-line arguments")
        case 2:
            sys.exit("Too few command-line arguments")
        case 3:
            if argument[1][-4:].lower() not in [".jpg",".png"] and argument[1][-5:].lower() != ".jpeg":
                sys.exit("Invalid input")
            elif argument[2][-4:].lower() not in [".jpg",".png"] and argument[2][-5:].lower() != ".jpeg":
                sys.exit("Invalid input")
            elif not compare_extensions(argument[1], argument[2]):
                sys.exit("Input and ouput have different extensions")
            else:
                return True
        case _:
            sys.exit("Too many command-line arguments")

def main():

    if eval_arguments(sys.argv):
        try:
            shirt = Image.open("shirt.png")
        except FileNotFoundError:
            sys.exit("shirt.png file does not exist")
        else:
            try:
                picture = Image.open(sys.argv[1])
            except FileNotFoundError:
                sys.exit("File does not exist")
            else:
                image = crop_to_square(picture)
                size = image.size
                out = ImageOps.fit(shirt, size)
                image.paste(out, out)
                image.save(sys.argv[2])


if __name__ == "__main__":
    main()
