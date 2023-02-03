import cv2
import pytesseract
import pyautogui
import keyboard
import subprocess as sp
import numpy as np

pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

#To take a screenshot of desired area, move your mouse cursor to corners of area
#and for start press s then for finish press e
while True:
    if keyboard.is_pressed("s"):
        a_posX, a_posY = pyautogui.position()
        break
while True:
    if keyboard.is_pressed("e"):
        b_posX, b_posY = pyautogui.position()
        break

pyautogui.screenshot("sample.png", region=(a_posX, a_posY, abs(b_posX-a_posX), abs(b_posY-a_posY)))
screenshot = cv2.imread("sample.png")

normalized_img = np.zeros((screenshot.shape[0], screenshot.shape[1]))
img = cv2.normalize(screenshot, normalized_img, 0, 255, cv2.NORM_MINMAX)
img = cv2.dilate(img, np.ones((1, 1)), iterations = 1)
img = cv2.threshold(img, 100, 255, cv2.THRESH_BINARY)[1]

file = open("recognized.txt", "w+")
    
config = r'-l eng+tur --oem 3 --psm 6'
text = pytesseract.image_to_string(img, config = config)
    
file.write(text)
file.write("\n")
file.close

programName = "notepad.exe"
fileName = "recognized.txt"
sp.Popen([programName, fileName])