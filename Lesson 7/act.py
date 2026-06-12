import cv2

face_c = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

cam = cv2.VideoCapture(0)

if not cam.isOpened():
    print("Error opening camera")
    exit()

while True:
    ret, frame = cam.read()

    if not ret:
        print("Camera failed to work")
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    face = face_c.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
    
    for (x, y, w, h) in face:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (203, 192, 255), 3)

    font = cv2.FONT_HERSHEY_PLAIN
    cv2.putText(frame, f'No. of people here are: {len(face)}', (10, 30), font, 1, (203, 192, 255), 1, cv2.LINE_AA)

    cv2.imshow("photobooth", frame)
    
    if cv2.waitKey(1) & 0xFF == ord("e"):
        break

cam.release()
cv2.destroyAllWindows()