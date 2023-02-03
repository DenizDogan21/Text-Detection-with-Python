# Text-Detection-with-Python
It is an application for text detection:
This script captures a screenshot of an area defined by pressing "s" and "e" keys on the keyboard, and then performs optical character recognition (OCR) on it using the PyTesseract library. The image is first normalized, dilated, and thresholded to improve the OCR results. The recognized text is then written to a text file and opened with Notepad. The OCR engine used is Tesseract with the language set to English and Turkish, and the OEM is set to 3 and PSM to 6.

How does it work ?
When the script is run, it waits for the user to press the "s" key to specify the starting point of the region to be captured as a screenshot. After the "s" key is pressed, the user moves the mouse cursor to the opposite corner of the desired area and presses the "e" key to specify the end point.
