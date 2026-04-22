import cv2
import mediapipe as mp

mp_face = mp.solutions.face_detection
face_detection = mp_face.FaceDetection(min_detection_confidence=0.6)

cap = cv2.VideoCapture(0)

print("Presiona 'q' para salir")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)
    h, w, _ = frame.shape

    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = face_detection.process(rgb)

    if results.detections:
        for detection in results.detections:
            bbox = detection.location_data.relative_bounding_box

            x = max(0, int(bbox.xmin * w) - 20)
            y = max(0, int(bbox.ymin * h) - 20)
            bw = min(w - x, int(bbox.width * w) + 40)
            bh = min(h - y, int(bbox.height * h) + 40)

            face_region = frame[y:y+bh, x:x+bw]
            blurred = cv2.GaussianBlur(face_region, (99, 99), 30)
            frame[y:y+bh, x:x+bw] = blurred

    cv2.imshow("Face Blur - MediaPipe + OpenCV", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
face_detection.close()
cv2.destroyAllWindows()
