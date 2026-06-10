import cv2
import matplotlib.pyplot as plt

img = cv2.imread('1.jpg')
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

h, w = img_rgb.shape[::2]

#Create a rectangle annotation
r_w, r_h = 1000, 1000
top_left = (30, 30)
bottom_right = (top_left[0] + r_w, top_left[1] + r_h )

#cv2.rectangle(image, pt1, pt2, color, thickness)
cv2.rectangle(img_rgb, top_left, bottom_right, (0, 255, 255), 5)

#Create another rectangle
r_w2, r_h2 = 300, 200
top_left2 = (40, 40)
bottom_right2 = (top_left2[0] + r_w2, top_left2[1] + r_h2 )

#cv2.rectangle(image, pt1, pt2, color, thickness)
cv2.rectangle(img_rgb, top_left2, bottom_right2,(255,0, 255), 5)


#Create a circle
ctr = (50, 50)
#cv2.circle(img, ctr, radius, color, thickness)
cv2.circle(img_rgb, ctr, 10, (255, 255, 0), 5)
#check

#COnnecting lines annotation

#cv2.line(img_rgb, pt1, pt2, color, thickness)
cv2.line(img_rgb, (50, 50), (50, 100), (0, 255, 255), 10)

# add text
cv2.putText(img_rgb, "hii", (70, 30), cv2.FONT_HERSHEY_COMPLEX, 32.5, (0, 0, 0), 5, cv2.LINE_AA)

#bidirection line
cv2.arrowedLine(img_rgb, (40, 30), (40, 60), (0, 255, 234), 10, tipLength= 0.7)

#display annotated img
plt.figure(figsize=(12, 8))
plt.imshow(img_rgb)
plt.title("picture")
plt.axis("off")
plt.show()