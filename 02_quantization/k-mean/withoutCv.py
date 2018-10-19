import matplotlib.pyplot as plt
# import cv2 as cv
import numpy as np
from math import sqrt

imgPath = '../assets/3_9.jpg'
imgOrigin = plt.imread(imgPath)
pixels = np.array(imgOrigin)
print(pixels.shape)

centroidValues = [pixels[x, x] for x in range(0, 128, 8)]
print(centroidValues)

pixelClusterAssignment = np.ones((128, 128))


def calculateNorm(vector):
    norm = sqrt(pow(vector[0, 0], 2)+pow(vector[0, 1], 2)+pow(vector[0, 2], 2))
    return norm


pixels[0, 0] - centroidValues[2]
x = (pixels[0, 0] - centroidValues[2])
x[0]
len(pixelClusterAssignment)


def clusterAssignment(centroidValues, pixelClusterAssignment, pixels):
    tempList = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    for i in range(len(pixelClusterAssignment)):
        for j in range(len(pixelClusterAssignment)):
            for k in range(16):
                tempList[k] = calculateNorm(pixels[i, j] - centroidValues[k])
                centroid = tempList.index(min(tempList))
                pixelClusterAssignment[i, j] = centroid

    return pixelClusterAssignment


clusterAssignment(centroidValues, pixelClusterAssignment, pixels)

print(pixelClusterAssignment[119, 120])


def updateCentroids(centroidValues, pixelClusterAssignment, pixels):

    for k in range(16):
        count = 0
        sum = [(0, 0, 0)]
        for i in range(128):
            for j in range(128):
                if pixelClusterAssignment[i, j] == k:
                    count = count+1
                    sum = sum + pixels[i, j]
        centroidValues[k] = sum/float(count)


def kMeansOneIter(centroidValues, pixelClusterAssignment, pixels):
    clusterAssignment(centroidValues, pixelClusterAssignment, pixels)
    updateCentroids(centroidValues, pixelClusterAssignment, pixels)


for y in range(30):

    kMeansOneIter(centroidValues, pixelClusterAssignment, pixels)


#check for convergence

cv30 = centroidValues
difference = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
kMeansOneIter(centroidValues, pixelClusterAssignment, pixels)

cv31 = centroidValues

for k in range(16):
    difference[k] = cv31[k] - cv30[k]

print(difference)
#Should be zero everywhere

#Finally, we will now go back to the large picture and replace each pixel's (r,g,b)
#values with value of the closest cluster centroid

#First we will match up each pixel in the large image with the centroid that is closest to it

pixelClusterAssignment1 = np.ones((512,512))

clusterAssignment(cv30,pixelClusterAssignment1,pixels1)
