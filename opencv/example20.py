# 轮廓发现

import cv2 as cv
import numpy as np

def contours_demo(image):
    dst = cv.GaussianBlur(image, (3, 3), 0)
    gray = cv.cvtColor(dst, cv.COLOR_BGR2GRAY)
    ret, binary = cv.threshold(gray, 0, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)
    cv.imshow("binary", binary)

    cloneImage, contours, heriachy = cv.findContours(binary, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
    cloneImage, contours, heriachy = cv.findContours(binary, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE) # EXTERNAL 轮廓外部
    cloneImage, contours, heriachy = cv.findContours(binary, cv.RETR_FLOODFILL, cv.CHAIN_APPROX_SIMPLE) # 轮廓填充
    for i, contour in enumerate(contours):
        cv.drawContours(image, contours, i, (0, 0, 255), 2)
        print(i)
    cv.imshow("detect output",image)




# ----------------------------------
print("Hello to Opencv world")
src = cv.imread("F:\\pythonwork\\opencv\\circle_test.jpg")  # 地址
# cv.namedWindow("input image", cv.WINDOW_AUTOSIZE) # 窗口设置名称，自由尺寸
# cv.imshow("origin", src)
t1 = cv.getTickCount()

contours_demo(src)

t2 = cv.getTickCount()
print((t2 - t1) / cv.getTickFrequency() * 1000)
cv.waitKey(00)

cv.destroyAllWindows()
