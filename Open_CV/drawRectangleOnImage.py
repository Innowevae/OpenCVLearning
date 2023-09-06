import numpy as np
import cv2
import matplotlib.pyplot as plt
%matplotlib inline

#draw balnk  image
blank_img=np.zeros(shape=(512,512,3) , dtype=np.int16)

# check shape
blank_img.shape
plt.imshow(blank_img)

#Draw rectangle on that image
cv2.rectangle(blank_img,pt1=(100,0),pt2=(400,200) ,color=(0,255,255), thickness=10)
plt.imshow(blank_img)