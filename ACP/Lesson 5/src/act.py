import cv2
import numpy as np

img = cv2.imread("../images/test.jpg")
if img is not None:
    img = cv2.resize(img, (600, int(img.shape[0] * (600 / img.shape[1]))))
    r_adj, g_adj, b_adj = 0, 0, 0
    mode = 0 

    while True:
        b, g, r = cv2.split(img)

        r = np.clip(r.astype(np.int16) + r_adj, 0, 255).astype(np.uint8)
        g = np.clip(g.astype(np.int16) + g_adj, 0, 255).astype(np.uint8)
        b = np.clip(b.astype(np.int16) + b_adj, 0, 255).astype(np.uint8)

        if mode == 1: g, b = np.zeros_like(g), np.zeros_like(b)
        elif mode == 2: r, b = np.zeros_like(r), np.zeros_like(b)
        elif mode == 3: r, g = np.zeros_like(r), np.zeros_like(g)

        processed = cv2.merge([b, g, r])
        cv2.imshow("Interactive Filters", processed)

        key = cv2.waitKey(1) & 0xFF
        if key == ord('q'): break
        elif key == ord('r'): mode = 1
        elif key == ord('g'): mode = 2
        elif key == ord('b'): mode = 3
        elif key == ord('i'): r_adj += 15
        elif key == ord('d'): b_adj -= 15
        elif key == 0x26 or key == 82: g_adj += 15       
        elif key == 0x28 or key == 84: r_adj -= 15       

    cv2.destroyAllWindows()

    filename = input("Filename: ")
    clean_name = "".join(c for c in filename if c.isalnum() or c in "._- ")
    if clean_name:
        cv2.imwrite(f"../images/{clean_name}", processed)