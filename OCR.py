import cv2 
import pytesseract

img = cv2.imread('frameSet/0-0.jpg')

# Adding custom options
custom_config = r'--oem 3 --psm 6 -l fin'
print(pytesseract.image_to_string(img, config=custom_config))
