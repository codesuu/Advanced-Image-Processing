import cv2 as cv
import matplotlib.image as pim
import matplotlib.pyplot as plt
import numpy as np

imgPath = './assets/3_6.jpg'
imgOrigin = pim.imread(imgPath)
Z = imgOrigin.reshape((-1, 3))
# convert to np.float32
Z = np.float32(Z)
# define criteria, number of clusters(K) and apply kmeans()
criteria = (cv.TERM_CRITERIA_EPS + cv.TERM_CRITERIA_MAX_ITER, 10, 1.0)
K = 8
ret, label, center = cv.kmeans(
    Z, K, None, criteria, 10, cv.KMEANS_RANDOM_CENTERS)
# Now convert back into uint8, and make original image
center = np.uint8(center)
res = center[label.flatten()]
res2 = res.reshape((imgOrigin.shape))
cv.imshow('res2', res2)
cv.waitKey(0)
cv.destroyAllWindows()
