#!/usr/bin/env python3
import cv2
import pytesseract

gray_img = cv2.imread("images/1.png",cv2.IMREAD_GRAYSCALE)
img = cv2.imread("images/1.png")
resized = cv2.resize(gray_img,(450,150))
(thresh, im_bw) = cv2.threshold(resized, 10, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
print(pytesseract.image_to_string(resized,config='--psm 7 -c tessedit_char_whitelist=0123456789.%'))
cv2.imshow("img",gray_img)
cv2.imshow("gray_img",resized)
cv2.waitKey(0)
cv2.destroyAllWindows()




"""
tamami = ""

# 0
crop = img[0:50, 0:40]
tamami += pytesseract.image_to_string(crop,lang="eng",config='--psm 7 -c tessedit_char_whitelist=0123456789.%')

# 1
crop = img[0:50, 40:60]
#(thresh, im_bw) = cv2.threshold(crop, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
tamami += pytesseract.image_to_string(crop,lang="eng",config='--psm 7 -c tessedit_char_whitelist=0123456789.%')
# 2
crop = img[0:50, 55:85]
tamami += pytesseract.image_to_string(crop,lang="eng",config='--psm 7 -c tessedit_char_whitelist=0123456789.%')

# 3
crop = img[0:50, 82:100]
tamami += pytesseract.image_to_string(crop,lang="eng",config='--psm 7 -c tessedit_char_whitelist=0123456789.%')

# 4
crop = img[0:50, 100:125]
tamami += pytesseract.image_to_string(crop,lang="eng",config='--psm 7 -c tessedit_char_whitelist=0123456789.%')

# 5
crop = img[0:50, 122:150]
tamami += pytesseract.image_to_string(crop,lang="eng",config='--psm 7 -c tessedit_char_whitelist=0123456789.%')

print(tamami)
"""
