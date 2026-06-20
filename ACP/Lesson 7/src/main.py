import cv2
import numpy as np
from tensorflow.keras.models import load_model

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
emotion_model = load_model('emotion_model.h5')
emotion_labels = ['Angry', 'Disgust', 'Fear', 'Happy', 'Neutral', 'Sad', 'Surprise']

np.set_printoptions(suppress=True, formatter={'float_kind':'{:0.4f}'.format})

cap = cv2.VideoCapture(0)
print("Webcam starting... Press 'q' to exit. LOOK AT THIS TERMINAL FOR PROBABILITIES.")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray_frame, scaleFactor=1.3, minNeighbors=5)

    for (x, y, w, h) in faces:
        pad = 10
        y1 = max(0, y - pad)
        y2 = min(frame.shape[0], y + h + pad)
        x1 = max(0, x - pad)
        x2 = min(frame.shape[1], x + w + pad)

        cv2.rectangle(frame, (x1, y1), (x2, y2), (255, 0, 0), 2)
        roi_gray = gray_frame[y1:y2, x1:x2]
        
        roi_resized = cv2.resize(roi_gray, (48, 48))
        roi_reshaped = np.reshape(roi_resized, (1, 48, 48, 1))
        prediction = emotion_model.predict(roi_reshaped, verbose=0)
        
        print(f"Probabilities: {prediction[0]}")
        
        max_index = int(np.argmax(prediction))
        predicted_emotion = emotion_labels[max_index]

        cv2.putText(frame, f"{predicted_emotion} ({prediction[0][max_index]:.2f})", 
                    (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

    cv2.imshow('Real-time Emotion Recognition', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()