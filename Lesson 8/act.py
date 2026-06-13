import cv2
import numpy as np

def op(ftype, frame):
    copy = frame.copy()
    gray = cv2.cvtColor(copy, cv2.COLOR_BGR2GRAY)

    if ftype == "red tint":
        copy[:,: ,0] = copy[:,: ,1] =  0
    elif ftype == "green tint":
        copy[:,: ,0] = copy[:,: ,2] =  0
    elif ftype == "blue tint":
        copy[:,: ,1] = copy[:,: ,2] =  0
    elif ftype == "sobel":
        sobel_x = cv2.Sobel(gray, cv2.CV_64F, 1, 0, 3)
        sobel_y = cv2.Sobel(gray, cv2.CV_64F, 0, 1, 3)    
        abs_x = np.absolute(sobel_x)
        abs_y = np.absolute(sobel_y)
        comb_sob = cv2.bitwise_or(abs_x.astype(np.uint8), abs_y.astype(np.uint8))
        copy = cv2.cvtColor(comb_sob, cv2.COLOR_GRAY2BGR)
    elif ftype == "canny":
        fr = cv2.Canny(gray, 100, 200)
        copy = cv2.cvtColor(fr, cv2.COLOR_GRAY2BGR)
    elif ftype == "cartoon":
        # CRITICAL FIX: Adaptive threshold requires a grayscale image
        bl = cv2.medianBlur(gray, 5)
        edge = cv2.adaptiveThreshold(bl, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 9)

        # Make the color version look like a watercolor painting
        col = cv2.bilateralFilter(frame, 9, 300, 300)
        copy = cv2.bitwise_and(col, col, mask=edge)    
    return copy


cam = cv2.VideoCapture(0)

if not cam.isOpened():
    print("Error opening camera")
    exit()

ftype = "original"

print("Choose your filter:\nr : red\nb : blue\ng : green\ns : sobel\nc : canny\nk: cartoon effect")

while True:
    ret, frame = cam.read()

    if not ret:
        print("Camera failed to work")
        break
    
    fin = op(ftype, frame)

    cv2.imshow("photobooth", fin)

    key = cv2.waitKey(1) & 0xFF

    if key == ord('r'):
        ftype = "red tint"
    elif key == ord('g'):
        ftype = "green tint"
    elif key == ord('b'):
        ftype = "blue tint"
    elif key == ord('s'):
        ftype = "sobel"
    elif key == ord('c'):
        ftype = "canny"
    elif key == ord('k'):
        ftype = "cartoon"
    elif key == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()

    

    




