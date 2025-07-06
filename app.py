import cv2
import numpy as np

# Open webcam
cap = cv2.VideoCapture(0)

def is_reddish_skin(avg_color):
    b, g, r = avg_color
    if r > 130 and r > g + 20 and r > b + 20:
        return True
    return False

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.resize(frame, (640, 480))
    x, y, w, h = 220, 140, 200, 200
    roi = frame[y:y+h, x:x+w]

    avg_color = cv2.mean(roi)[:3]

    if is_reddish_skin(avg_color):
        status = "Abnormal (Reddish Skin)"
        color = (0, 0, 255)
    else:
        status = "Normal Skin"
        color = (0, 255, 0)

    cv2.rectangle(frame, (x, y), (x+w, y+h), color, 2)
    cv2.putText(frame, status, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, color, 2)
    cv2.imshow("UV Therapy Skin Monitor", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
