import cv2



img = cv2.imread("1.jpg")

if img is None:
    print(f"Error: Could not load image '{"1.jpg"}'.")
    exit()

small = cv2.resize(img, (200, 200))
medium = cv2.resize(img, (400, 400))
large = cv2.resize(img, (600, 600))


cv2.imwrite("input_image_small.jpg", small)
cv2.imwrite("input_image_medium.jpg", medium)
cv2.imwrite("input_image_large.jpg", large)
print("Resized images saved successfully!")


cv2.imshow("Small Image (200x200)", small)
cv2.imshow("Medium Image (400x400)", medium)
cv2.imshow("Large Image (600x600)", large)


print("Press any key to exit.")
cv2.waitKey(0)
cv2.destroyAllWindows()