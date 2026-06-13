import cv2
import numpy as np

image_path = "../images/test.jpg" 

img = cv2.imread(image_path)

if img is not None:
    img = cv2.resize(img, (600, int(img.shape[0] * (600 / img.shape[1]))))
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray_blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    edges = cv2.Canny(gray_blurred, 100, 200)
    
    cv2.imshow("gray + blurred", gray_blurred)
    cv2.imshow("canny edge", edges)
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print(f" couldnt read {image_path}")
    print("doesnt work")