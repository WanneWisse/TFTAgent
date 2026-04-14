import pygetwindow as gw
from mss import mss
import numpy as np
import cv2

# Find window (change title!)
window = gw.getWindowsWithTitle("League of Legends")[0]

# Get window position
left, top = window.left, window.top
width, height = window.width, window.height


monitor = {
    "top": top,
    "left": left,
    "width": width,
    "height": height
}

sct = mss()

while True:
    img = sct.grab(monitor)
    frame = np.array(img)
    frame = cv2.cvtColor(frame, cv2.COLOR_BGRA2BGR)

    cv2.imshow("Window Capture", frame)

    if cv2.waitKey(1) == ord("q"):
        break

cv2.destroyAllWindows()