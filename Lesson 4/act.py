import cv2
import numpy as np

def display(window_name, img):
    cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)
    cv2.resizeWindow(window_name, 800, 600)
    
    cv2.imshow(window_name, img)
    
    cv2.waitKey(0)          
    cv2.destroyAllWindows()

def op(imgpath):
    img = cv2.imread(imgpath)
    if img is None:
        print("Img has no value")
        return 
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    display("gray",img_gray)
    cv2.waitKey(0)
    while True:
        print("Select operation (1-6) you want to do:\n1) Sobel Edge\n2) Canny edge\n3) Laplacian Edge\n4) Gaussian Smoothing\n5) Median filtering\n6) Exit")
        choice = int(input("Enter a choice: "))
        if choice == 1:
            #Sobel edge
            sobel_x = cv2.Sobel(img_gray, cv2.CV_64F, 1, 0, 3)
            sobel_y = cv2.Sobel(img_gray, cv2.CV_64F, 0, 1, 3)
            
            abs_x = np.absolute(sobel_x)
            abs_y = np.absolute(sobel_y)
            
            # Fixed typo from np.unit8 to np.uint8
            comb_sob = cv2.bitwise_or(abs_x.astype(np.uint8), abs_y.astype(np.uint8))
            display("Sobel Edge", comb_sob)
        elif choice == 2:
            #Canny edge
            lower = int(input("Enter lower threshold - default 100 and 200:"))
            higher = int(input("Enter higher threshold - default 100 and 200:"))
            im = cv2.Canny(img_gray, lower, higher)
            display("Canny Edge", im)
        elif choice == 3:
            #laplacian
            lap = cv2.Laplacian(img_gray, cv2.CV_64F)
            
            # Take the absolute value
            abs_lap = np.absolute(lap)
            
            # Normalize the image so the brightest edge scales all the way up to 255
            cv2.normalize(abs_lap, abs_lap, 0, 255, cv2.NORM_MINMAX)
            
            # Safely cast to 8-bit unsigned integer
            display("Laplacian Edge", abs_lap.astype(np.uint8))
            
        elif choice == 4:
            #gaussian
            ksize = int(input("Enter a ksize (must be odd): "))
            b_img = cv2.GaussianBlur(img, (ksize, ksize), 0)
            display("Gaussian Blur", b_img)
            
        elif choice == 5:
            #median filter
            ksize = int(input("Enter a ksize (must be odd): "))
            m_img = cv2.medianBlur(img, ksize)
            display("Median Filter", m_img)
        
        elif choice == 6:
            print("bye")
            return

        else:
            print("Invalid Choice. Try again")
            

op("1.jpg")