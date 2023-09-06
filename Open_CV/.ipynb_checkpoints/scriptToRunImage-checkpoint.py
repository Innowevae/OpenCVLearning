import cv2 

img=cv2.imread('anshul.jpg')

when true:
    cv2.imshow('anshul',img)
    if cv2.waitKey(1) & 0xFF ==27:
        break