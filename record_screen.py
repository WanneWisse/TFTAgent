import cv2
import numpy as np
from mss import mss

sct = mss()

# Pick monitor (change this index!)
monitor_number = 2  # 1 = primary screen, 2 = second screen

monitor = sct.monitors[monitor_number]

# Video writer setup
fourcc = cv2.VideoWriter_fourcc(*"XVID")
out = cv2.VideoWriter(
    "screen_record.avi",
    fourcc,
    20.0,
    (monitor["width"], monitor["height"])
)

print(f"Recording monitor {monitor_number}... Press 'q' to stop.")

while True:
    img = sct.grab(monitor)
    frame = np.array(img)

    # Convert BGRA → BGR
    frame = cv2.cvtColor(frame, cv2.COLOR_BGRA2BGR)

    out.write(frame)
    cv2.imshow("Recording", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

out.release()
cv2.destroyAllWindows()