import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

image = cv2.imread('m63219_res_SIP_420-444_res_output.tif',0)
thresh = cv2.threshold(image, 80, 255, cv2.THRESH_BINARY_INV)[1]

kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5,5))
#erosion = cv2.erode(image,kernel,iterations = 1)
opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel)
#closing = cv2.morphologyEx(image, cv2.MORPH_CLOSE, kernel)

result = 255 - opening
cv2.imshow('thresh', thresh)
cv2.imshow('opening', opening)
cv2.imshow('result', result)

print(pytesseract.image_to_string(result))
cv2.waitKey()