# 图像二值化
# 三角阈值二值化

import cv2 as cv
import numpy as np

# 全局阈值
def threshold_demo(image):
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    # ret, binary = cv.threshold(gray, 0, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)
    ret, binary = cv.threshold(gray, 0, 255, cv.THRESH_BINARY | cv.THRESH_TRIANGLE) # 不同方法
    ret, binary = cv.threshold(gray, 127, 255, cv.THRESH_BINARY ) #自己设置阈值需要删除后面的方法
    print("threshold value %s"%ret)
    cv.imshow("binary", binary)

# 局部阈值，自适应二值化
def local_threshold_demo(image):
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    dst = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 25, 10) # 自适应阈值,25位置必须为奇数
    dst = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 25, 10) #

def custom_threshold(image):
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    h, w = gray.shape[:2]
    m = np.reshape(gray, [1, w * h])
    mean = m.sum() / (w + h)
    print("mean: ", mean)
    ret, binary = cv.threshold(gray, mean, 100, cv.THRESH_BINARY)
    cv.imshow("binary2",binary)

src = cv.imread("F:\\C++\\test\\3432.png")  # 地址
print("Hello to Opencv world")
cv.namedWindow("input image", cv.WINDOW_AUTOSIZE) # 窗口设置名称，自由尺寸

t1 = cv.getTickCount()
threshold_demo(src)
local_threshold_demo(src)
custom_threshold(src)
t2 = cv.getTickCount()
print((t2 - t1)/cv.getTickFrequency() * 1000)
cv.waitKey(3000)

cv.destroyAllWindows()
