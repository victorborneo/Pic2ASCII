import numpy as np

def reshape(array, x):
    matrix = []
    line = []

    counter = 0
    for value in array:
        if counter >= x:
            matrix.append(line)
            line = [value]
            counter = 1
        else:
            counter += 1
            line.append(value)

    matrix.append(line)
    return matrix

def parse_areas(image, x):
    array = []
    image_x, image_y = image.size
    pixels = reshape(list(image.getdata()), image_x)

    y = max(x // 3, 1)
    if x > image_x:
        x = image_x
    if y > image_y:
        y = image_y // 3

    size_x, size_y = image_x // x, image_y // y

    for i in range(image_y // size_y):
        line = []

        for j in range(image_x // size_x):
            if j > 1024:
                break

            r, g, b, counter = 0, 0, 0, 0
            for k in range(size_y):
                for l in range(size_x):
                    pixel = pixels[i * size_y + k][j * size_x + l]

                    r += pixel[0]
                    g += pixel[1]
                    b += pixel[2]
                    counter += 1

            line.append((r // counter, g // counter, b // counter))
        array.append(line)

    return array

def convert_to_ascii(array):
    ascii_ = ""

    pixel_ascii_map = "@%#*+=-:. "

    for line in array:
        for r, g, b in line:
            brightness = 0.2126 * r + 0.7152 * g + 0.0722 * b
            char = int(brightness / 255 * len(pixel_ascii_map))

            ascii_ += pixel_ascii_map[char]

        ascii_ += "\n"

    return ascii_