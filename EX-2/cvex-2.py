import cv2 

im  = cv2.imread("index.jpg")

image_rgb1 = cv2.cvtColor(im, cv2.COLOR_RGB2BGR)
image_rgb2 = cv2.cvtColor(im, cv2.COLOR_RGB2HSV)
image_rgb3 = cv2.cvtColor(im, cv2.COLOR_RGB2GRAY)
image_rgb4 = cv2.cvtColor(im, cv2.COLOR_RGB2YUV)

cv2.imshow('RGB2BGR', image_rgb1)
cv2.imshow('RGB2HSV', image_rgb2)
cv2.imshow('RGB2GRAY', image_rgb3)
cv2.imshow('RGB2YUV', image_rgb4)

cv2.waitKey(0)
cv2.destroyAllWindows()
