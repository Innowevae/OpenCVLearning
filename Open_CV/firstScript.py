import cv2 

img=cv2.imread('anshul.jpg')

while True:
    cv2.imshow('anshul',img)
    
    # Wait for 1 ms AND press Esc key
    if cv2.waitKey(1) & 0xFF ==27:
        break

cv2.destroyAllWindows()