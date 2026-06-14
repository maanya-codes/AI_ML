import cv2
import numpy as np

cam = cv2.VideoCapture(0)

if not cam.isOpened():
    print("Camera is not working")
    exit()

while True:
    ret, frame = cam.read()
    
    if not ret:
        print("Camera is not working")
        break

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    #detect skin color range

    low_skin = np.array([0, 20, 70], dtype=np.uint8)
    up_skin = np.array([20, 255, 255], dtype=np.uint8)

    #create a mask to detect the skin color only
    mask = cv2.inRange(hsv, low_skin, up_skin)

    #apply on video

    res = cv2.bitwise_and(frame, frame, mask=mask)

    #in the masked frame, find hand shape
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    if contours:
        max_contour = max(contours, key=cv2.contourArea)

    if cv2.contourArea(max_contour) > 500:
        x, y, w, h = cv2.boundingRect(max_contour)
        cv2.rectangle(frame, (x, y), (x + w, y + h),(203, 192, 255), 2 ) 

    #center circle in hand
    c_x = int((x+w)/2)
    c_y = int((y + h)/2)
    cv2.circle(frame, (c_x, c_y), 5, (203, 192, 255), -1)

    cv2.imshow("Original Video", frame)
    cv2.imshow("Filtered Video", res)

    if cv2.waitKey(1) & 0xFF == ord("e"):
        break

cam.release()
cv2.destroyAllWindows()







