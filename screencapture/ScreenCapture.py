import pyautogui
import cv2
import numpy as np

# Create an Empty window
cv2.namedWindow("Live", cv2.WINDOW_NORMAL)

# Resize this window
cv2.resizeWindow("Live", 480, 270)

while True:
    # Take screenshot using PyAutoGUI
    img = pyautogui.screenshot()

    frame = np.array(img)

    frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)

    # Optional: Display the recording screen
    cv2.imshow('Live', frame)

    key = cv2.waitKeyEx(25) & 0xFF
    print(key)

    if key == ord('q'):
        break

cv2.destroyAllWindows()