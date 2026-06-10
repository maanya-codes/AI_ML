import cv2

#load image
img = cv2.imread("example.jpg")

#resize window w/o resize img
cv2.namedWindow('Loaded Image', cv2.WINDOW_NORMAL)

cv2.resizeWindow('Loaded Image', 800, 500)

#putting img

cv2.imshow('Loaded Image', img)




cv2.waitKey(0)
cv2.destroyAllWindows()

print(f"printing the {img.shape}....")