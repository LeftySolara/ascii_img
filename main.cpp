#include <stdio.h>
#include <opencv4/opencv2/opencv.hpp>

using namespace cv;

int main(int argc, char **argv)
{
    if (argc != 2) {
        printf("usage: AsciiArt <ImagePath>\n");
        return -1;
    }

    Mat image;
    image = imread(argv[1], 1);

    if (!image.data) {
        printf("No image data\n");
        return -1;
    }

    printf("Successfully loaded image!\n");
    printf("Image size: %d x %d\n", image.cols, image.rows);

    return 0;
}