import sys
import numpy
from PIL import Image

def main():
    if len(sys.argv) != 2:
        print("usage: asciiArt <ImagePath>")
        return

    image = Image.open(sys.argv[1])
    print("Successfully loaded image")
    print("Image size: {} x {}".format(image.width, image.height))

    pixels = numpy.asarray(image, numpy.intc)
    print()
    print("Successfully created pixel matrix")

    brightness_matrix = numpy.zeros((image.height, image.width), numpy.uint8)
    for y in range(0, image.height):
        for x in range(0, image.width):
            brightness = (pixels[y][x][0] + pixels[y][x][1] + pixels[y][x][2]) // 3
            brightness_matrix[y][x] = brightness

    print("Successfully created brightness matrix")


if __name__ == "__main__":
    main()
