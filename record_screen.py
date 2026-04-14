import pygetwindow as gw
from mss import mss
import numpy as np
import cv2

def showFrame(frame, scale):
    # Resize (scale down to half)
    scale = 0.3
    frame = cv2.resize(frame, (0, 0), fx=scale, fy=scale)
    cv2.imshow("Window Capture", frame)
# Find window (change title!)
window = gw.getWindowsWithTitle("League of Legends (TM) Client")[0]

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

out_width = 1920
out_height = 1080

# --- Video writer setup ---
fourcc = cv2.VideoWriter_fourcc(*"mp4v")
out = cv2.VideoWriter("output.mp4", fourcc, 20.0, (out_width, out_height))


while True:
    img = sct.grab(monitor)
    frame = np.array(img)
    frame = cv2.cvtColor(frame, cv2.COLOR_BGRA2BGR)
    # Resize frame
    frame = cv2.resize(frame, (out_width, out_height))

    #showFrame(frame,0.3)
    # Write to file
    out.write(frame)
    

    if cv2.waitKey(1) == ord("q"):
        break

# Cleanup
out.release()
cv2.destroyAllWindows()