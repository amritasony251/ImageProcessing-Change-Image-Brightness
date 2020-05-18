from PIL import Image
import numpy as np
import cv2

temp = 100

img = cv2.imread("g.jpeg")
img_out = img.copy()

width, height, bit = np.shape(img)

for j in range(0,height) :
 for i in range(0,width) :
    img_out[i][j][0] = temp + img_out[i][j][0]
    img_out[i][j][1] = temp + img_out[i][j][1]
    img_out[i][j][2] = temp + img_out[i][j][2]
    
minm = np.amin(img_out)
maxm = np.amax(img_out) 

for j in range(0,height) :
 for i in range(0,width) :
    if(img_out[i][j][0] > 255):
      img_out[i][j][0] = 255*(img_out[i][j][0] - minm)/(maxm-minm) 
      img_out[i][j][1] = 255*(img_out[i][j][1] - minm)/(maxm-minm) 
      img_out[i][j][2] = 255*(img_out[i][j][2] - minm)/(maxm-minm)  

cv2.imshow('image',img_out)
cv2.waitKey(0)
           
