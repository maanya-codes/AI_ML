import cv2
import numpy as np
import matplotlib.pyplot as plt


img = cv2.imread('example.jpg')

#rotate
(h, w)= img.shape[:2]
center = (w//2, h//2)
M = cv2.getRotationMatrix2D(center, 90, 1.0)
final = cv2.warpAffine(img, M, (w, h))

rgb = cv2.cvtColor(final, cv2.COLOR_BGR2RGB)


plt.imshow(rgb)
plt.title("picture")
plt.show()

# increase brightness
bright = np.ones(img.shape, dtype="uint8") * 50
bimg = cv2.add(img, bright)
rgb = cv2.cvtColor(bimg, cv2.COLOR_BGR2RGB)


plt.imshow(rgb)
plt.title("picture")
plt.show()

