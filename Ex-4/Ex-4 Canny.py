import numpy as np
import cv2 as cv
img = cv.imread('img.jpg',0)
edges = cv.Canny(img,100,200)
res = np.hstack((img, edges))
cv.imshow('Edge detected', res)
cv.waitKey(0)
cv.destroyAllWindows()
