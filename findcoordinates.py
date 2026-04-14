import cv2
import time

def mouse_click(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        print(f"Clicked at: X={x}, Y={y}")

cap = cv2.VideoCapture("output.mp4")
cap.set(cv2.CAP_PROP_POS_FRAMES, 100)

ret, frame = cap.read()

if ret:
    cv2.imshow("Frame 100", frame)
    cv2.setMouseCallback("Frame 100", mouse_click)    
    cv2.waitKey(0)

ret, frame = cap.read()


# width_first_shopbox = 190
# height_first_shopbox = 140