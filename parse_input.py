# import cv2

# video_path = "output.mp4"
# cap = cv2.VideoCapture(video_path)

# frame_count = 0

# while cap.isOpened():
#     ret, frame = cap.read()

#     if not ret:
#         break  # video finished

#     frame_count += 1

#     cv2.line(frame, (500, 950), (500, 400), (0, 255, 0), 3)
#     # Example: show frame
#     cv2.imshow("Frame", frame)

#     if cv2.waitKey(1) == ord("q"):
#         break

# cap.release()
# cv2.destroyAllWindows()

# print("Total frames read:", frame_count)

import cv2
import time

def mouse_click(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        print(f"Clicked at: X={x}, Y={y}")

cap = cv2.VideoCapture("output.mp4")

# cv2.namedWindow("Frame")
# cv2.setMouseCallback("Frame", mouse_click)

cap.set(cv2.CAP_PROP_POS_FRAMES, 100)

ret, frame = cap.read()
width_shopbox = 190
height_shopbox = 140

if ret:
    for i in range(5):
        cv2.rectangle(frame, (508 + i * width_shopbox, 925), (690 + i * width_shopbox, 1065), (0, 255, 0), 3)
    cv2.imshow("Frame 100", frame)
    cv2.setMouseCallback("Frame 100", mouse_click)
    
    cv2.waitKey(0)

# cap.read()
# while cap.isOpened():
#     ret, frame = cap.read()
#     if not ret:
#         break

#     cv2.imshow("Frame", frame)
#     time.sleep(10) 
    # if cv2.waitKey(1) == ord("q"):
    #     break

cap.release()
cv2.destroyAllWindows()