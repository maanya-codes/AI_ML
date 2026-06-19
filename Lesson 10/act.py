import cv2
import mediapipe as mp
import numpy as np

from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
import screen_brightness_control as sbc

Hands = mp.solutions.hands

hands = Hands.Hands(min_detection_confidence=0.7, min_tracking_tracking=0.7)

draw = mp.solution.drawing_utils

TH = Hands.HandLandmark.THUMB_TIP

TX = Hands.HandLandmark.INDEX_FINGER_TIP

#volume control

dev = AudioUtilities.GetDefaultOutputDevice() if hasattr(AudioUtilities,
 "GetDefaultOutputDevice") else AudioUtilities.GetSpeaker()





cam = cv2.VideoCapture(0)

if not cam.isOpened():
    print("Camera is not working")
    exit()

cv2.namedWindow("Hand Gesture Based Project", cv2.WINDOW_NORMAL)
while True:
    ret, frame = cam.read()
    
    if not ret:
        print("Camera is not working")
        break

    




    if cv2.waitKey(1) & 0xFF == ord("e"):
        break

cam.release()
cv2.destroyAllWindows()







