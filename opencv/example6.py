import cv2 as cv
import numpy as np

# 模糊操作

# 中值模糊
def blur_demo(image):
    dst = cv.blur(image, (5, 5))
    cv.imshow("blur_demo",dst)

# 均值模糊
def median_blur_demo(image):
    dst = cv.medianBlur(image, 5)
    cv.imshow("median_blur_demo",dst)

# 自定义 模糊
def custom_blur_demo(image):
    kernel = np.ones([5, 5], np.float32)/25
    kernel = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]], np.float32) #锐化算子
    dst = cv.filter2D(image, -1, kernel=kernel)
    cv.imshow("custom_blur_demo",dst)

src = cv.imread("F:\\pythonwork\\opencv\\1.jpg")  # 地址
cv.namedWindow("input image", cv.WINDOW_AUTOSIZE) # 窗口设置名称，自由尺寸
cv.imshow("input image",src) # 打开图片
blur_demo(src)
median_blur_demo(src)
custom_blur_demo(src)
cv.waitKey(3000)