
import matplotlib.image as pim
import matplotlib.pyplot as plt
import numpy as np

imgPath = '../assets/3_6.jpg'
imgOrigin = pim.imread(imgPath)

hist, bins = np.histogram(imgOrigin.flatten(), 256, [0, 256])
cdf = hist.cumsum()
cdf_m = np.ma.masked_equal(cdf, 0)
cdf_m = (cdf_m - cdf_m.min()) * 255 / (cdf_m.max()-cdf_m.min())
cdf = np.ma.filled(cdf_m, 0).astype('uint8')
imgEq = cdf[imgOrigin]

plt.subplot('211'), plt.imshow(imgOrigin, 'gray'), plt.title('Origin Image')
plt.subplot('212'), plt.imshow(imgEq, 'gray'), plt.title('Equalised Image')
plt.show()
