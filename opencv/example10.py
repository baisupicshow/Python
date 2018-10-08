# 直方图均衡化提高对比度

from matplotlib import pyplot as plt
import cv2 as cv
import numpy as np

def equalHist_demo(image):
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    dst = cv.equalizeHist(gray)
    cv.imshow("equalHist_demo", dst)

def clahe_demo(image):
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    clahe = cv.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
    dst = clahe.apply(gray)
    cv.imshow("clahe", dst)


src = cv.imread("F:\\C++\\test\\3432.png")  # 地址
cv.namedWindow("input image", cv.WINDOW_AUTOSIZE) # 窗口设置名称，自由尺寸
cv.imshow("input image",src) # 打开图片
t1 = cv.getTickCount()
clahe_demo(src)
t2 = cv.getTickCount()
print((t2 - t1)/cv.getTickFrequency() * 1000)
cv.waitKey(3000)

cv.destroyAllWindows()
