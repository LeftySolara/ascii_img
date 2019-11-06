import sys
import numpy
from PIL import Image

def main():
    if len(sys.argv) != 2:
        print("usage: asciiArt <ImagePath>")
        return

    image = Image.open(sys.argv[1])
    print("Successfully loaded image!")
    print("Image size: {} x {}".format(image.width, image.height))

    pixels = numpy.asarray(image)

    print("Iterating through pixel contents:")
    for y in range (0, image.height):
        for x in range(0, image.width):
            print(pixels[y][x])
        print()

if __name__ == "__main__":
    main()
