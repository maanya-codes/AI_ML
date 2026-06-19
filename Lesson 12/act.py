import cv2, time, numpy as np
import mediapipe as mp

#set mediapipe
H = mp.solutions.hands
TIP = H.HandLandmark

ids = {
"thumb": TIP.THUMB_TIP,
"index": TIP.INDEX_FINGER_TIP,
"middle": TIP.MIDDLE_FINGER_TIP,
"ring": TIP.RING_FINGER_TIP,
"pinky": TIP.PINKY_TIP,
}

hands = H.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.7)
draw = mp.solutions.drawing_utils
#Some variable for managing the state of filter config
paused = False
freeze = None
pinch_on = False
#set camera

cam = cv2.VideoCapture(1)
if not cam.isOpened():
    print("Error: Camera cover is closed")
    exit()

cv2.namedWindow("Gesture Control Photo APP", cv2.WINDOW_NORMAL)

#Main loop
while True:
    if paused:
        cv2.imshow("Gesture Control Photo APP", freeze)
        k = cv2.waitKey(50) & 0xFF
        if k == ord("q"):
            break
        if k == 27:
            paused = False
            pinch_on = False
            try:
                cv2.destroyAllWindows("Captured (Esc/close to resume)")
            except:
                pass
            continue
    try:
        if cv2.getWindowProperty("Captured (Esc/close to resume)", cv2.WND_PROP_VISIBLE) <= 0:
            paused = False
            pinch_on = False
    except cv2.error:
        paused = False
        pinch_on = False
        continue

