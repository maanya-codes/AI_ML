import cv2

#Use cascade classifier folder to do the activity
face = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

#trigger camera
cam = cv2.VideoCapture(0)

#checking of camera
if not cam.isOpened():
    print("Camera is covered.")
    exit()

#logic

while True:
    #capture video frame by frame
    ret , frame = cam.read()
    #checking of camera
    if not ret:
        print("Error in capturing the video")
        break

    #cvt to gray
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    face_p = face.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    for (x, y, w, h) in face_p:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (203, 192, 255), 3)

    cv2.imshow("photobooth", frame)
    #end the program
    if cv2.waitKey(1) & 0xFF == ord("g"):
        break

cam.release()
cv2.destroyAllWindows()