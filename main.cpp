#include <iostream>
#include <opencv4/opencv2/opencv.hpp>

using namespace cv;
using std::cout;
using std::endl;

Mat loadImage(char *path)
{
    Mat image = imread(path, IMREAD_COLOR);
    
    if (!image.data) {
        cout << "Error: could not load image" << endl;
        exit(-1);
    }
    cout << "Successfully loaded image!" << endl;
    cout << "Image size: " << image.cols << " x " << image.rows << endl;
    
    return image;
}

void iterateBrightness(Mat image)
{
    int rows = image.rows;
    int cols = image.cols;
    int avg;

    cout << "Iterating through pixel brightnesses:" << endl;
    for (int y = 0; y < rows; ++y) {
        for (int x = 0; x < cols; ++x) {
            const Vec3b pixel = image.at<Vec3b>(y, x);
            avg = (pixel.val[0] + pixel.val[1] + pixel.val[2]) / 3;
            cout << avg << endl;
        }
    }
}

int main(int argc, char **argv)
{
    if (argc != 2) {
        printf("usage: AsciiArt <ImagePath>\n");
        return -1;
    }

    Mat image = loadImage(argv[1]);
    iterateBrightness(image);

    return 0;
}