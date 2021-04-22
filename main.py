import os
from PIL import Image
from fractions import Fraction


def parse_areas(image, x, y):
    array = []
    image_x, image_y = image.size
    pix_vals = list(image.getdata())
    size_y, size_x = int(image_y / y), int(image_x / x)

    for i in range(y):
        line = []

        for j in range(x):

            r, g, b, counter = 0, 0, 0, 0
            for k in range(size_y):
                for l in range(size_x):
                    pixel = pix_vals[j * size_x + i * image_x * size_y + l + k * image_x]

                    r += pixel[0]
                    g += pixel[1]
                    b += pixel[2]
                    counter += 1

            line.append((r // counter, g // counter, b // counter))
        array.append(line)

    return array

def convert_to_ascii(array):
    ascii_ = ""
    pixel_ascii_map = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\\|()1{}[]?-_+~i!lI;:,\"^`"
    # pixel_ascii_map = "`^\",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"
    for line in array:
        for r, g, b in line:
            brightness = 0.2126 * r + 0.7152 * g + 0.0722 * b
            char = int(brightness * len(pixel_ascii_map) / 255)

            ascii_ += pixel_ascii_map[char]

        ascii_ += "\n"

    return ascii_

def main():
    while True:
        directory = input("Image file directory: ")

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
