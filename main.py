import os
from PIL import Image
from functions import *

def main():
    message = "DISCLAIMER: Windows .txt files automatically add new lines after 1024 characters, " \
        "so using too high width values will crop the output. If you want the best quality output, " \
        " nonetheless set width to the image X resolution and use another text reader."
    print(f"{'='*len(message)}\n{message}\nDefault width set to 800.\n{'='*len(message)}")

    width = 800 # The higher this value is, the better the output will be, but as satted above, high values will get weird results on Windows .txt files

    while True:
        directory = input("Image file directory (Type a number to change width): ")  # Try using bg.jpg

        if directory.isdigit():
            width = int(directory)
            print(f"New width set to {width}")
            continue

        try:
            im = Image.open(directory)
        except (FileNotFoundError, OSError):
            print("File not found.")
            continue    

        f = open("output.txt", "w")
        f.write(convert_to_ascii(parse_areas(im, width)))
        f.close()

        os.system("output.txt")


if __name__ == "__main__":
    main()
