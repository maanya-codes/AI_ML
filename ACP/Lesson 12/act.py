import cv2
import mediapipe as mp
import numpy as np
import time


mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.7, min_tracking_confidence=0.7)
mp_draw = mp.solutions.drawing_utils


FILTERS = ['None', 'Grayscale', 'Sepia', 'Negative', 'Blur']
current_filter_idx = 0


last_action_time = 0
debounce_delay = 1.0  
status_message = ""
status_message_expiry = 0

def apply_filter(frame, filter_name):
    
    if filter_name == 'Grayscale':
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        return cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)
        
    elif filter_name == 'Sepia':
        
        kernel = np.array([[0.272, 0.534, 0.131],
                           [0.349, 0.686, 0.168],
                           [0.393, 0.769, 0.189]])
        sepia = cv2.transform(frame, kernel)
        return np.clip(sepia, 0, 255).astype(np.uint8)
        
    elif filter_name == 'Negative':
        return cv2.bitwise_not(frame)
        
    elif filter_name == 'Blur':
        return cv2.GaussianBlur(frame, (15, 15), 0)
        
    return frame

def get_distance(p1, p2):
    """Calculates Euclidean distance between two landmarks."""
    return np.sqrt((p1.x - p2.x)**2 + (p1.y - p2.y)**2)


cap = cv2.VideoCapture(0)

print("Starting Gesture-Controlled Camera System...")
print("- Thumb + Index: Capture Photo")
print("- Thumb + Middle/Ring/Pinky: Switch Filters")

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    
    frame = cv2.flip(frame, 1)
    h, w, c = frame.shape

    
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(rgb_frame)

    current_time = time.time()
    gesture_detected = None

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            
            mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
            
            landmarks = hand_landmarks.landmark
            
            # Key landmark indices: Thumb tip = 4, Index tip = 8, Middle tip = 12, Ring tip = 16, Pinky tip = 20
            thumb = landmarks[4]
            index = landmarks[8]
            middle = landmarks[12]
            ring = landmarks[16]
            pinky = landmarks[20]

            # Threshold distance for a 'touch' gesture (normalized coordinates)
            touch_threshold = 0.05

            # Check distances between thumb and other fingers
            if get_distance(thumb, index) < touch_threshold:
                gesture_detected = "capture"
            elif (get_distance(thumb, middle) < touch_threshold or 
                  get_distance(thumb, ring) < touch_threshold or 
                  get_distance(thumb, pinky) < touch_threshold):
                gesture_detected = "switch_filter"

    # Process Actions with Debounce Control
    if gesture_detected and (current_time - last_action_time > debounce_delay):
        if gesture_detected == "capture":
            # Apply filter first so the saved picture includes the active visual effect
            photo_to_save = apply_filter(frame.copy(), FILTERS[current_filter_idx])
            filename = f"photo_{int(current_time)}.png"
            cv2.imwrite(filename, photo_to_save)
            
            status_message = f"CAPTURED: {filename}"
            status_message_expiry = current_time + 2.0  # Show message for 2 seconds
            
        elif gesture_detected == "switch_filter":
            current_filter_idx = (current_filter_idx + 1) % len(FILTERS)
            status_message = f"Filter changed to {FILTERS[current_filter_idx]}"
            status_message_expiry = current_time + 1.5

        last_action_time = current_time

    # Render Selected Visual Filter
    frame = apply_filter(frame, FILTERS[current_filter_idx])

    # Overlay Real-Time UI Text Feedback
    cv2.putText(frame, f"Filter: {FILTERS[current_filter_idx]}", (20, 40), 
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)

    # Show active status messages (e.g., photo saved alert)
    if current_time < status_message_expiry:
        cv2.putText(frame, status_message, (20, h - 30), 
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2, cv2.LINE_AA)

    # Display Window
    cv2.imshow("Gesture Camera System", frame)

    # Press 'q' to break out and exit safely
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()