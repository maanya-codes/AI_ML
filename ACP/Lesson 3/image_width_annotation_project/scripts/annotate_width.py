import cv2
import os

img_path = os.path.join("..", "original_images", "1.jpg")
save_path = os.path.join("..", "output_images", "annotated_1.jpg")

img = cv2.imread(img_path)

if img is None:
    print(f"Error: Could not find or read image at {img_path}")
    exit()

h, w = img.shape[:2]
mid_y = int(h * 0.5)

cv2.arrowedLine(img, (0, mid_y), (int(w * 0.4), mid_y), (0, 255, 0), 3, tipLength=0.05)
cv2.arrowedLine(img, (w, mid_y), (int(w * 0.6), mid_y), (0, 255, 0), 3, tipLength=0.05)

text = f"{w} px"
font = cv2.FONT_HERSHEY_SIMPLEX
scale = 1.0
thick = 2
color = (0, 255, 0)

text_w, text_h = cv2.getTextSize(text, font, scale, thick)[0]
text_x = int((w - text_w) / 2)
text_y = int(mid_y + (text_h / 2))

cv2.putText(img, text, (text_x, text_y), font, scale, color, thick, cv2.LINE_AA)

os.makedirs(os.path.dirname(save_path), exist_ok=True)
cv2.imwrite(save_path, img)
print("Annotated image saved successfully!")