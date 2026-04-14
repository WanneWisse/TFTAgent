import cv2

video_path = "output.mp4"
cap = cv2.VideoCapture(video_path)

frame_count = 0

while cap.isOpened():
    ret, frame = cap.read()

    if not ret:
        break  # video finished

    frame_count += 1

    # Example: show frame
    cv2.imshow("Frame", frame)

    if cv2.waitKey(1) == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()

print("Total frames read:", frame_count)