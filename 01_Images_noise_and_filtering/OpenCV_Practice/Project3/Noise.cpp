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
	//	i = rand() % src_img.cols; // �̹����� ��ũ�� ������ ���� �� ����, x ��ǥ��
	//	j = rand() % src_img.rows; // �̹����� ��ũ�� ������ ���� �� ����, y ��ǥ��

	//	int salt_or_pepper = (rand() % 2) * 255; // �����ϰ� 0 �Ǵ� 255, 0�̸� ����, 255�� �ұ�

	//	if (src_img.type() == CV_8UC1) // �׷��̷��� �����̶��
	//		src_img.at<uchar>(j, i) = salt_or_pepper; // �����ϰ� ���õ� �ȼ��� 0 �Ǵ� 255�� ���� 
	//	else if (src_img.type() == CV_8UC3) // 3ä�� �÷� �����̶��
	//	{
	//		// �����ϰ� ���õ� �ȼ��� 0 �Ǵ� 255�� ����, ��� �Ǵ� �������� ����� ���� �� �÷� ä�ο� ������ ���� ��. (0, 0, 0) �Ǵ� (255, 255, 255). 
	//		src_img.at<cv::Vec3b>(j, i)[0] = salt_or_pepper; // B ä��
	//		src_img.at<cv::Vec3b>(j, i)[1] = salt_or_pepper; // G ä��
	//		src_img.at<cv::Vec3b>(j, i)[2] = salt_or_pepper; // R ä��
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
