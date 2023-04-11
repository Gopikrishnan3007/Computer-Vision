import numpy as np
import cv2 as cv

im = cv.imread('index.jpg',1)
img = cv.resize(im,(650,650))

def affine(img):
    rows,cols,ch = img.shape[:3]
    pts1 = np.float32([[50,50],[200,50],[50,200]])
    pts2 = np.float32([[10,100],[200,50],[100,200]])
    M = cv.getAffineTransform(pts1,pts2)
    res = cv.warpAffine(img,M,(cols,rows))
    return res

def perspective(img):
    rows,cols,ch = img.shape[:3]
    pts1 = np.float32([[46,65],[300,65],[46,300],[300,300]])
    pts2 = np.float32([[10,10],[350,10],[10,350],[350,350]])
    M = cv.getPerspectiveTransform(pts1,pts2)
    res = cv.warpPerspective(img,M,(cols,rows))
    return res

cv.imshow('Actual',img)
cv.waitKey()
cv.imshow('Affine Image',affine(img))
cv.waitKey()
cv.imshow('Perspective Image',perspective(img))
cv.waitKey()
cv.destroyAllWindows()
