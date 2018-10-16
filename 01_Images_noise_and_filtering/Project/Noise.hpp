#pragma once
#include <opencv2/opencv.hpp>
#include <opencv2/core.hpp>
#include <opencv2/highgui.hpp>
#include <stdlib.h>
#include <time.h>

void salt_pepper(cv::Mat src_img, int n);
cv::Mat gaussian_nosie(cv::Mat src_img, double average, double sigma);

