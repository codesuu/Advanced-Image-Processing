
def main():
    import cv2
    import numpy as np
    import matplotlib.pyplot as plt

    # original image
    img = cv2.imread('./assets/stationery.jpg', cv2.IMREAD_GRAYSCALE)

    # otsu
    _, imgOtsu = cv2.threshold(
        img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    # erosion
    kernel = np.ones((5, 5), np.uint8)
    erosion = cv2.erode(imgOtsu, kernel, iterations=1)

    # dilation
    dilation = cv2.dilate(imgOtsu, kernel, iterations=1)

    # opening
    opening = cv2.morphologyEx(imgOtsu, cv2.MORPH_OPEN, kernel)

    # closing
    closing = cv2.morphologyEx(imgOtsu, cv2.MORPH_CLOSE, kernel)

    plt.subplot(1, 3, 1), plt.imshow(imgOtsu, 'gray')
    plt.subplot(1, 3, 2), plt.imshow(opening, 'gray')
    plt.subplot(1, 3, 3), plt.imshow(closing, 'gray')
    plt.show()


if __name__ == '__main__':
    main()
