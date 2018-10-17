
import matplotlib.image as pim
import matplotlib.pyplot as plt
import numpy as np


def viewer(*imgSrcs):
    img1 = imgSrcs[0]
    img2 = imgSrcs[1]

    hist1, _ = np.histogram(img1[3].flatten(), 256, [0, 256])
    hist2, _ = np.histogram(img2[3].flatten(), 256, , [0, 256])

    plt.subplot(221), plt.imshow(img1, 'gray'), plt.title('Origin Image')
    plt.subplot(222), plt.plot(
        hist1, color='slategrey'), plt.title('Origin Histogram')
    plt.subplot(223), plt.imshow(img2, 'gray'), plt.title('Hist-Eq Image')
    plt.subplot(224), plt.plot(
        hist2, color='slategrey'), plt.title('Hist-Eq Histogram')
    plt.xlim([0, 256])
    plt.show()


imgPath = './assets/3_6.jpg'
imgOrigin = pim.imread(imgPath)

# get rows, coloums, channels from original image
imgRows, imgCols, imgChan = imgOrigin.shape

# 그레이 스케일 이미지 변환

imgGray = np.dot(imgOrigin[..., :3], [0.299, 0.587, 0.114])
# for row in range(imgRows):
#     for cols in range(imgCols):
#         b = imgOrigin[row, cols][0]
#         g = imgOrigin[row, cols][1]
#         r = imgOrigin[row, cols][2]
#         gray = (b + g + r) / 3.0

# 히스토그램 계산
hist = [0] * 256  # 히스토그램
for row in range(imgRows):
    for col in range(imgCols):
        value = int(imgGray[row][col])
        hist[value] += 1

# 누적 히스토그램 계산
histCum = [0] * 256  # 누적 히스토그램
for idx, _ in enumerate(histCum):
    histCum[idx] = sum(hist[:idx + 1])

nHistCum = [0] * 256
for idx, _ in enumerate(histCum):
    nHistCum[idx] = histCum[idx] / (imgRows * imgCols)

# 평활화 계산
imgEqGray = np.array([[0] * imgCols] * imgRows)
for row in range(imgRows):
    for col in range(imgCols):
        imgEqGray[row][col] = histCum[int(imgGray[row][col])] * 255

# 이미지 출력
viewer(imgOrigin, imgEqGray)
