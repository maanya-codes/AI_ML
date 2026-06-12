import cv2
import numpy as np

TITLE = "IMAGE"

def apply_filter(img, filt_type):
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
    elif filt_type == "i":  # Changed from "ir" to a single character
        copy[:,:, 2] = cv2.add(copy[:,:, 2], 50)
    elif filt_type == "d":  # Changed from "dg" to a single character
        copy[:,:, 1] = cv2.subtract(copy[:,:, 1], 50)
    else:
        print("Invalid key")
        return None
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
    # Moved terminal input entirely to window-based key presses for a smoother flow
    print("Click on the image window and press keys for filters:")
    print(" 'r'=red, 'g'=green, 'b'=blue, 'i'=ir, 'd'=dg. Press 'e' to exit.")
    
    display(img) # Display the base image first to accept key presses

    while True:
        # Wait for a key press continuously
        key = cv2.waitKey(0) & 0xFF
        char_key = chr(key).lower()

        if char_key == "e":
            print("Exiting program")
            break
        
        filt_img = apply_filter(img, char_key)
        
        # If a valid filter key was pressed, close the old window and open a new one
        if filt_img is not None:
            cv2.destroyAllWindows() # Closes the image
            display(filt_img)       # Reloads the new filter

    cv2.destroyAllWindows()