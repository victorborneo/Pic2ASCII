import os
from PIL import Image
from functions import *

def main():
    while True:
        directory = input("Image file directory: ")  # Try using bg.jpg

        try:
            im = Image.open(directory)
        except (FileNotFoundError, OSError):
            print("File not found.")
            continue

        res_x, res_y = im.size[0] // 2, im.size[1] // 5        

        f = open("output.txt", "w")
        f.write(convert_to_ascii(parse_areas(im, res_x, res_y)))
        f.close()

        os.system("output.txt")


if __name__ == "__main__":
    main()
