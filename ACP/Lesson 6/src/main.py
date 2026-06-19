import cv2
import numpy as np
from tensorflow.keras.models import load_model

MODEL_PATH = "src/emotion_model.h5"

EMOTION_LABELS = ['Angry', 'Disgust', 'Fear', 'Happy', 'Sad', 'Surprise', 'Neutral']

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

try:
    emotion_model = load_model(MODEL_PATH)
except Exception:
    raise FileNotFoundError(f"Model not found at {MODEL_PATH}")

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        break

    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray_frame, scaleFactor=1.3, minNeighbors=5)

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
        
        roi_gray = gray_frame[y:y + h, x:x + w]
        
        try:
            roi_resized = cv2.resize(roi_gray, (48, 48), interpolation=cv2.INTER_AREA)
            roi_normalized = roi_resized / 255.0
            roi_reshaped = np.reshape(roi_normalized, (1, 48, 48, 1))

            prediction = emotion_model.predict(roi_reshaped, verbose=0)
            max_index = int(np.argmax(prediction))
            predicted_emotion = EMOTION_LABELS[max_index]

            cv2.putText(
                frame, 
                predicted_emotion, 
                (x, y - 10), 
                cv2.FONT_HERSHEY_SIMPLEX, 
                0.9, 
                (0, 255, 0), 
                2, 
                cv2.LINE_AA
            )
        except Exception:
            pass

    cv2.imshow('Real-time Face Emotion Detection', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()