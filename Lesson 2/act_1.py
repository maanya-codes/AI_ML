import cv2
import matplotlib.pyplot as plt

img = cv2.imread('example.jpg')

#bgr to rgb
rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
plt.imshow(rgb)
plt.title("picture")
plt.show()

#bgr to gray
bw = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
plt.imshow(bw, cmap='gray')
plt.title("picture")
plt.show()

#crop
crp = img[100:300, 100:400]
saved = cv2.cvtColor(crp, cv2.COLOR_BGR2RGB)
plt.imshow(saved)
plt.title("picture")
plt.show()

