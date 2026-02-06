import pyautogui
import cv2
import numpy as np

class ScreenReader:
    def capture(self):
        screenshot = pyautogui.screenshot()
        img = np.array(screenshot)
        return cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
