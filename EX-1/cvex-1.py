import cv2
#Input image
input = cv2.imread('index.jpg')
#Get input size
height, width = input.shape[:2]
#Desired "pixelated" size
w, h = (1920, 1232)
#Resize input to "pixelated" size
temp = cv2.resize(input, (w, h), interpolation=cv2.INTER_LINEAR)
#Initialize output image
output1 = cv2.resize(temp, (width, height), interpolation=cv2.INTER_NEAREST)
cv2.imshow("rocket 24 .jpg", output1)

#Input image
input = cv2.imread('index.jpg')
#Get input size
height, width = input.shape[:2]
#Desired "pixelated" size
w, h = (256, 256)
#Resize input to "pixelated" size
temp = cv2.resize(input, (w, h), interpolation=cv2.INTER_LINEAR)
#Initialize output image
output2 = cv2.resize(temp, (width, height), interpolation=cv2.INTER_NEAREST)
cv2.imshow("rocket 8.jpg", output2)

#Input image
input = cv2.imread('index.jpg')
#Get input size
height, width = input.shape[:2]
#Desired "pixelated" size
w, h = (16, 16)
#Resize input to "pixelated" size
temp = cv2.resize(input, (w, h), interpolation=cv2.INTER_LINEAR)
#Initialize output image
output3 = cv2.resize(temp, (width, height), interpolation=cv2.INTER_NEAREST)
cv2.imshow("rocket 4.jpg", output3)

#Input image
input = cv2.imread('index.jpg')
#Get input size
height, width = input.shape[:2]
#Desired "pixelated" size
w, h = (2, 2)
#Resize input to "pixelated" size
temp = cv2.resize(input, (w, h), interpolation=cv2.INTER_LINEAR)
#Initialize output image
output4 = cv2.resize(temp, (width, height), interpolation=cv2.INTER_NEAREST)
cv2.imshow("rocket 1.jpg", output4)

