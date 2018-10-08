# 边缘检测

import cv2 as cv
import numpy as np

def sonbel_demo(image):
    grad_x = cv.Sobel(image, cv.CV_32F, 1, 0)
    grad_x = cv.Scharr(image, cv.CV_32F, 1, 0) # 边缘增强
    grad_y = cv.Sobel(image, cv.CV_32F, 0, 1)
    gradx = cv.convertScaleAbs(grad_x)
    grady = cv.convertScaleAbs(grad_y)
    cv.imshow("gradient_x", gradx)
    cv.imshow("gradient_y", grady)

    gradxy = cv.addWeighted(gradx, 0.5, grady, 0.5, 0)
    cv.imshow("gradient", gradxy)


# 拉普拉斯算子
def lapalian_demo(image):
    dst = cv.Laplacian(image, cv.CV_32F)
    lpls = cv.convertScaleAbs(dst)
    cv.imshow("lapalian", lpls)

# 自定义拉普拉斯
def lapalian_demo_self_design(image):
    kernel = np.array([[1, 1, 1], [1, -8, 1], [1, 1, 1]])
    dst = cv.filter2D(image, cv.CV_32F, kernel=kernel)
    lals = cv.convertScaleAbs(dst)
    cv.imshow("self_design", lals)

# ----------------------------------
print("Hello to Opencv world")
src = cv.imread("F:\\pythonwork\\opencv\\1.jpg")  # 地址
cv.namedWindow("input image", cv.WINDOW_AUTOSIZE) # 窗口设置名称，自由尺寸

t1 = cv.getTickCount()
sonbel_demo(src)
lapalian_demo(src)
lapalian_demo_self_design(src)
t2 = cv.getTickCount()
print((t2 - t1)/cv.getTickFrequency() * 1000)
cv.waitKey(0)

cv.destroyAllWindows()

