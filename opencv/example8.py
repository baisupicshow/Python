# 边缘保留滤波 EPF
import cv2 as cv
import numpy as np

# 边缘保留滤波，高斯磨皮
def bi_demo(image):
    dst = cv.bilateralFilter(image, 0, 100, 15)
    cv.imshow("bi_demo",dst)

# 均值迁移
def shift_demo(image):
    dst = cv.pyrMeanShiftFiltering(image, 10, 20)
    cv.imshow("shift_demo", dst)

src = cv.imread("F:\\C++\\test\\3432.png")  # 地址
cv.namedWindow("input image", cv.WINDOW_AUTOSIZE) # 窗口设置名称，自由尺寸
cv.imshow("input image",src) # 打开图片
t1 = cv.getTickCount()
bi_demo(src)
shift_demo(src)
t2 = cv.getTickCount()
print((t2 - t1)/cv.getTickFrequency() * 1000)
cv.waitKey(3000)