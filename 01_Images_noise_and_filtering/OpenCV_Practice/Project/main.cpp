#include "Noise.hpp"
#include <iostream>


int main(void)
{

	cv::Mat img = cv::imread("lenna.png");
	cv::resize(img, img, cv::Size(300, 300));
	cv::Mat salt_pepper_img = img.clone();
	cv::Mat gaussian_img;

	// 노이즈 생성
	salt_pepper(salt_pepper_img, 10.0);
	gaussian_img = gaussian_nosie(img, 0.0, 30.0);

	cv::Mat sp_average_img;
	cv::Mat ga_average_img;
	cv::Mat sp_gaussian_img;
	cv::Mat ga_gaussian_img;
	cv::Mat sp_median_img;
	cv::Mat ga_median_img;

	//cv::blur(salt_pepper_img, sp_average_img, cv::Size(5, 5));
	//cv::blur(gaussian_img, ga_average_img, cv::Size(5, 5));
	//cv::GaussianBlur(salt_pepper_img, sp_gaussian_img, cv::Size(5, 5), 1.5);
	//cv::GaussianBlur(gaussian_img, ga_gaussian_img, cv::Size(5, 5), 1.5);
	cv::medianBlur(salt_pepper_img, sp_median_img, 5);
	//cv::medianBlur(gaussian_img, ga_median_img, 5);



	// 창 정렬
	//cv::namedWindow("original Img",CV_WINDOW_AUTOSIZE);
	//cv::namedWindow("salt_and_pepper Img",CV_WINDOW_AUTOSIZE);
	//cv::namedWindow("gaussian Img",CV_WINDOW_AUTOSIZE);
	//cv::namedWindow("sp img with average",CV_WINDOW_AUTOSIZE);
	cv::namedWindow("sp img with median",CV_WINDOW_AUTOSIZE);
	//cv::namedWindow("sp img with gaussian",CV_WINDOW_AUTOSIZE);
	//cv::namedWindow("ga img with average",CV_WINDOW_AUTOSIZE);
	//cv::namedWindow("ga img with median",CV_WINDOW_AUTOSIZE);
	//cv::namedWindow("ga img with gaussian",CV_WINDOW_AUTOSIZE);

	int img_pos = img.size().width;
	//cv::moveWindow("original Img", 0, img_pos*1.5);
	//cv::moveWindow("salt_and_pepper Img",img_pos,img_pos);
	//cv::moveWindow("gaussian Img", img_pos, img_pos*2);
	//cv::moveWindow("sp img with average",img_pos*2,img_pos );
	//cv::moveWindow("sp img with median", img_pos*3, img_pos);
	//cv::moveWindow("sp img with gaussian", img_pos*4,img_pos);
	//cv::moveWindow("ga img with average", img_pos*2,img_pos*2);
	//cv::moveWindow("ga img with median", img_pos*3, img_pos*2);
	//cv::moveWindow("ga img with gaussian", img_pos*4, img_pos*2);

	//cv::imshow("original Img", img);
	//cv::imshow("salt_and_pepper Img", salt_pepper_img);
	//cv::imshow("gaussian Img", gaussian_img);

	/*
	cv::imshow("sp img with average", sp_average_img);
	cv::imshow("ga img with average", ga_average_img);
	*/
	cv::imshow("sp img with median", sp_median_img);
	/*
	cv::imshow("ga img with median", ga_median_img);
	cv::imshow("sp img with gaussian", sp_gaussian_img);
	cv::imshow("ga img with gaussian", ga_gaussian_img);
*/
	cv::waitKey(0);
}