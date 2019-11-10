import sys
import numpy
import shutil
from PIL import Image


def loadImage(path):
    try:
        image = Image.open(path)
        print("Successfully loaded image")
        print("Image size: {} x {}".format(image.width, image.height))
        return image
    except FileNotFoundError:
        print("Error: file not found")
        exit(1)


def resizeImage(image):
    term_size = shutil.get_terminal_size()
    image = image.resize((term_size.columns, term_size.lines))

    return image


def createPixelMatrix(image):
    pixels = numpy.asarray(image, numpy.intc)
    print("Successfully created pixel matrix")

    return pixels


def createBrightnessMatrix(pixel_matrix):
    rows = pixel_matrix.shape[0]
    cols = pixel_matrix.shape[1]
    brightness_matrix = numpy.zeros((rows, cols), numpy.uint8)

    for y in range(0, rows):
        for x in range(0, cols):
            brightness = (pixel_matrix[y][x][0]
                          + pixel_matrix[y][x][1]
                          + pixel_matrix[y][x][2]) // 3
            brightness_matrix[y][x] = brightness

    print("Successfully created brightness matrix")
    return brightness_matrix


def createAsciiMatrix(brightness_matrix):
    rows = brightness_matrix.shape[0]
    cols = brightness_matrix.shape[1]
    ascii_matrix = numpy.zeros((rows, cols), dtype=str)
    ascii_chars = "`^\",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"

    for y in range(0, rows):
        for x in range(0, cols):
            char_index = (brightness_matrix[y][x] / 255) * len(ascii_chars)
            ascii_matrix[y][x] = ascii_chars[int(char_index) % len(ascii_chars)]

    print("Successfully created ASCII matrix")
    return ascii_matrix


def printMatrix(matrix):
    rows = matrix.shape[0]
    cols = matrix.shape[1]

    for y in range(0, rows):
        for x in range(0, cols):
            print(matrix[y][x], end="")


def main():
    if len(sys.argv) != 2:
        print("usage: ascii-img <ImagePath>")
        return

    image = loadImage(sys.argv[1])
    image = resizeImage(image)

    pixel_matrix = createPixelMatrix(image)
    brightness_matrix = createBrightnessMatrix(pixel_matrix)
    ascii_matrix = createAsciiMatrix(brightness_matrix)

    printMatrix(ascii_matrix)


if __name__ == "__main__":
    main()

