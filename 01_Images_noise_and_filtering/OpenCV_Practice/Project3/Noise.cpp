#pragma once
#include "Noise.hpp"

void salt_pepper(cv::Mat src_img, int n)
{
	srand((int)time(NULL));
	double noise_percentage = 40.;
	int noise_points = (int)(((double)src_img.rows * src_img.cols * src_img.channels()) * noise_percentage / 100.);
	for (int count = 0; count < noise_points; count++) {
		int row = rand() % src_img.rows;
		int col = rand() % src_img.cols;
		int channel = rand() % src_img.channels();

		uchar* pixel = src_img.ptr<uchar>(row) + (col * src_img.channels()) + channel;

		*pixel = (rand() % 2 == 1) ? 255 : 0;
	}
	//int i, j;
	//srand((int)time(NULL));

	//

	//for (int k = 0; k < n; k++)
	//{
	//	i = rand() % src_img.cols; // 이미지의 열크기 내에서 랜덤 수 생성, x 좌표값
	//	j = rand() % src_img.rows; // 이미지의 행크기 내에서 랜덤 수 생성, y 좌표값

	//	int salt_or_pepper = (rand() % 2) * 255; // 랜덤하게 0 또는 255, 0이면 후추, 255면 소금

	//	if (src_img.type() == CV_8UC1) // 그레이레벨 영상이라면
	//		src_img.at<uchar>(j, i) = salt_or_pepper; // 랜덤하게 선택된 픽셀에 0 또는 255을 대입 
	//	else if (src_img.type() == CV_8UC3) // 3채널 컬러 영상이라면
	//	{
	//		// 랜덤하게 선택된 픽셀에 0 또는 255을 대입, 흰색 또는 검정색을 만들기 위해 세 컬러 채널에 동일한 것이 들어감. (0, 0, 0) 또는 (255, 255, 255). 
	//		src_img.at<cv::Vec3b>(j, i)[0] = salt_or_pepper; // B 채널
	//		src_img.at<cv::Vec3b>(j, i)[1] = salt_or_pepper; // G 채널
	//		src_img.at<cv::Vec3b>(j, i)[2] = salt_or_pepper; // R 채널
	//	}
	//}
}


cv::Mat gaussian_nosie(cv::Mat src_img, double average, double sigma)
{
	cv::Mat noise_img(src_img.size(), CV_16SC3);
	cv::randn(noise_img, cv::Scalar::all(average), cv::Scalar::all(sigma));
	cv::Mat temp_img;
	src_img.convertTo(temp_img, CV_16SC3);
	cv::addWeighted(temp_img, 1.0, noise_img, 1.0, 0.0, temp_img);
	temp_img.convertTo(temp_img, src_img.type());
	return temp_img;
}
