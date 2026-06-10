import cv2

#load image
img = cv2.imread('example.jpg')

#chg to grayscale
bw = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#resize img
resized = cv2.resize(bw, (224, 224))

cv2.imshow('Loaded Image', resized)


key = cv2.waitKey(0)

if key == ord('s'):
    cv2.imwrite('grayscale_resized.jpg', resized)
    print("Saved.")
else:
    print("Not saved.")

cv2.destroyAllWindows()

print(f"printing the {resized.shape}....")


