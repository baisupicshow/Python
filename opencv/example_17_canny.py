# Canny算法——边缘提取
'''
1.高斯模糊 — GaussianBlur
2.灰度转换 — cvtColor
3.计算梯度 — Sobel / Scharr
4,.非最大信号抑制
5.高低阈值输出二值图像
'''
import cv2 as cv
import numpy as np

#
def edge_demo(image):
    blurred = cv.GaussianBlur(image, (3, 3), 0)
    gray = cv.cvtColor(blurred, cv.COLOR_BGR2GRAY)
    # X gradient
    xgrad = cv.Sobel(gray, cv.CV_16SC1, 1, 0)
    ygrad = cv.Sobel(gray, cv.CV_16SC1, 0, 1)
    edge_output = cv.Canny(xgrad, ygrad, 50, 150)
    edge_output = cv.Canny(gray, 56, 150)
    cv.imshow("Canny_edge", edge_output)

    dst = cv.bitwise_and(image, image, mask=edge_output)
    cv.imshow("color Edge", dst)



# ----------------------------------
print("Hello to Opencv world")
src = cv.imread("F:\\pythonwork\\opencv\\1.jpg")  # 地址
# cv.namedWindow("input image", cv.WINDOW_AUTOSIZE) # 窗口设置名称，自由尺寸
cv.imshow("origin", src)
t1 = cv.getTickCount()
edge_demo(src)

t2 = cv.getTickCount()
print((t2 - t1)/cv.getTickFrequency() * 1000)
cv.waitKey(0)

cv.destroyAllWindows()
