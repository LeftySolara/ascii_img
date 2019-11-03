#include <iostream>
#include <opencv4/opencv2/opencv.hpp>

using namespace cv;
using std::cout;
using std::endl;

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

    int cols = image.cols;
    int rows = image.rows;

    cout << "Successfully loaded image!" << endl;
    cout << "Image size: " << cols << " x " << rows << endl;

    // If the image matrix is continuous, it's less overhead
    // to process it as a single, long row.
    if (image.isContinuous()) {
        cols *= rows;
        rows = 1;
    }
    for (int i = 0; i < rows; ++i) {
        const Vec3b *pixels = image.ptr<Vec3b>(i);
        for (int j = 0; j < cols; ++j)
            cout << pixels[j] << endl;
    }

    return 0;
}