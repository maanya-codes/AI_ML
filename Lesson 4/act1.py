import cv2
import numpy as np

def display(window_name, img):
    cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)
    cv2.resizeWindow(window_name, 800, 600)
    
    cv2.imshow(window_name, img)
    
    cv2.waitKey(0)          
    cv2.destroyAllWindows()

img = cv2.imread("1.jpg")
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
display("gray",img_gray)
cv2.waitKey(0)
cv2.destroyAllWindows()
print(f"printing the {img.shape}....")