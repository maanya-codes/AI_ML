import cv2
import numpy as np

img = cv2.imread("1.jpg")

if img is None:
    print("Error: Could not find or read '1.jpg' in the current folder!")
    exit()

height, width = img.shape[:2]

rotated_img = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)

brightened_img = cv2.convertScaleAbs(img, alpha=1.0, beta=50)

start_y, end_y = int(height * 0.25), int(height * 0.75)
start_x, end_x = int(width * 0.25), int(width * 0.75)
cropped_img = img[start_y:end_y, start_x:end_x]

cv2.imwrite("1_rotated.jpg", rotated_img)
cv2.imwrite("1_brightened.jpg", brightened_img)
cv2.imwrite("1_cropped.jpg", cropped_img)
print("All transformations saved successfully!")

cv2.namedWindow("Original Image", cv2.WINDOW_NORMAL)
cv2.namedWindow("Transform 1: Rotated", cv2.WINDOW_NORMAL)
cv2.namedWindow("Transform 2: Brightened", cv2.WINDOW_NORMAL)
cv2.namedWindow("Transform 3: Cropped", cv2.WINDOW_NORMAL)

cv2.imshow("Original Image", img)
cv2.imshow("Transform 1: Rotated", rotated_img)
cv2.imshow("Transform 2: Brightened", brightened_img)
cv2.imshow("Transform 3: Cropped", cropped_img)

print("Press any key on an image window to exit.")
cv2.waitKey(0)
cv2.destroyAllWindows()