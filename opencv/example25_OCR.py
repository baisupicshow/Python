# 数字验证码识别
# 二值化去干扰

import numpy as np
import cv2 as cv
import pytesseract as tess
from PIL import Image

def recognize_text(image):
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    ret, binary = cv.threshold(gray, 0, 255, cv.THRESH_BINARY_INV | cv.THRESH_OTSU)
    kernel = cv.getStructuringElement(cv.MORPH_RECT, (1, 2))
    binl = cv.morphologyEx(binary, cv.MORPH_RECT, kernel)
    open_out = cv.morphologyEx(binl, cv.MORPH_OPEN, (2, 1))
    cv.imshow("binary-image", open_out)

    cv.bitwise_not(open_out, open_out)
    textImage = Image.fromarray(open_out)
    text = tess.image_to_string(textImage)
    print("识别结果： %s"%text)


print("Hello to Opencv world")
src = cv.imread("F:\\pythonwork\\opencv\\2.jpg")  # 地址

# cv.namedWindow("input image", cv.WINDOW_AUTOSIZE) # 窗口设置名称，自由尺寸
cv.imshow("origin", src)
t1 = cv.getTickCount()

recognize_text(src)

t2 = cv.getTickCount()
print((t2 - t1) / cv.getTickFrequency() * 1000)
cv.waitKey(4000)

cv.destroyAllWindows()

