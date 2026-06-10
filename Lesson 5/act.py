import cv2
import numpy as np

TITLE = "IMAGE"

def filter(img, filt_type):
    copy = img.copy()
    if filt_type == "r":
        copy[:,:, 0] = 0
        copy[:,:, 1] = 0
    elif filt_type == "g":
        copy[:,:, 0] = 0
        copy[:,:, 2] = 0
    elif filt_type == "b":
        copy[:,:, 1] = 0
        copy[:,:, 2] = 0
    elif filt_type == "ir":
        copy[:,:, 2] = cv2.add(copy[:,:, 2], 50)
    elif filt_type == "dg":
        copy[:,:, 1] = cv2.subtract(copy[:,:, 1], 50)
    else:
        print("Invalid key")
        cv2.destroyAllWindows()
    return copy

def display(img):
    cv2.namedWindow(TITLE, cv2.WINDOW_NORMAL)
    cv2.resizeWindow(TITLE, 800, 500)
    cv2.imshow(TITLE, img)

img = cv2.imread('1.jpg')

if img is None:
    print("ERROR: '1.jpg' was not found in this folder!")
    input("Press Enter to close...")
else:
    print("Press keys for filter ( r, g, b, ir, dg). Press e to exit")
    choice = input("Your choice: ")
    if choice == "e":
        print("Exiting program")
    else:
        filt_img = filter(img, choice)
        display(filt_img)
        
        while True:
            key = cv2.waitKey(0) & 0xFF
            if key == ord('e'):
                break
                
        cv2.destroyAllWindows()