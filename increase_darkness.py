from PIL import Image
import numpy as np
import cv2

temp = 50

img = cv2.imread("gg.png")
img_out = img.copy()

width, height, bit = np.shape(img)

for j in range(0,height) :
 for i in range(0,width) :
    img_out[i][j][0] = img_out[i][j][0] - temp 
    if(img_out[i][j][0] < 0) :
      img_out[i][j][0] = 0
    img_out[i][j][1] = img_out[i][j][1] - temp
    if(img_out[i][j][1] < 0) :
      img_out[i][j][1] = 0
    img_out[i][j][2] = img_out[i][j][2] - temp
    if(img_out[i][j][2] < 0) :
      img_out[i][j][2] = 0

cv2.imshow('image',img_out)
cv2.waitKey(0)
           
