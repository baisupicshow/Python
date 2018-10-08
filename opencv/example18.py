# 直线检测

import cv2 as cv
import numpy as np


def line_detect(image):
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    cv.imshow("gray", gray)
    edges = cv.Canny(gray, 50, 150, apertureSize=3)
    lines = cv.HoughLines(edges, 1.0, np.pi / 180, 140, 10, 0)
    '''
HoughLinesP(image, rho, theta, threshold, lines=None, minLineLength=None, maxLineGap=None) 
1.image： 必须是二值图像，推荐使用canny边缘检测的结果图像；
2.rho：线段以像素为单位的距离精度，double类型的，推荐用1.0
3.theta： 线段以弧度为单位的角度精度，推荐用numpy.pi/180
4.threshod：累加平面的阈值参数，int类型，超过设定阈值才被检测出线段，值越大，基本上意味着检出的线段越长，检出的线段个数越少。根据情况推荐先用100试试
5.lines：线条的输出向量。
6.minLineLength：线段以像素为单位的最小长度。
7.maxLineGap：同一方向上两条线段判定为一条线段的最大允许间隔（断裂），超过了设定值，则把两条线段当成一条线段，值越大，允许线段上的断裂越大，越有可能检出潜在的直线段'''
    print(lines)
    for line in lines:
        rho, theta = line[0]
        a = np.cos(theta)
        b = np.sin(theta)
        print(a, b)
        x0 = a * rho
        y0 = b * rho
        x1 = int(x0 + 1000 * (-b))
        y1 = int(y0 + 1000 * (a))
        x2 = int(x0 - 1000 * (-b))
        y2 = int(y0 - 1000 * (a))
        cv.line(image, (x1, y1), (x2, y2), (0, 0, 255), 2)
    cv.imshow("image_line", image)








# ----------------------------------
print("Hello to Opencv world")
src = cv.imread("F:\\pythonwork\\opencv\\3.jpg")  # 地址
# cv.namedWindow("input image", cv.WINDOW_AUTOSIZE) # 窗口设置名称，自由尺寸
cv.imshow("origin", src)
t1 = cv.getTickCount()
line_detect(src)

t2 = cv.getTickCount()
print((t2 - t1) / cv.getTickFrequency() * 1000)
cv.waitKey(3000)

cv.destroyAllWindows()

