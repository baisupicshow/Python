# 金字塔

import numpy as np
import cv2 as cv


# 高斯金字塔
def pyramid_demo(image):
    level = 3
    temp = image.copy()
    pyramid_images = []
    for i in range(level):
        dst = cv.pyrDown(temp)
        pyramid_images.append(dst)
        cv.imshow("pyramid_down_" + str(i),dst)
        temp = dst.copy()
    return pyramid_images
# 拉普拉斯金字塔
def lapalian_demo(image):
    pyramid_image = pyramid_demo(image)
    level = len(pyramid_image)
    for i in range(level - 1, -1):
        if (i - 1) < 0:
            expand = cv.pyrUp(pyramid_image[i], dstsize=image.shape[:2])
            lpls = cv.subtract(image, expand)
            cv.imshow("lapalian_down_" + str(i), lpls)
        else:
            expand = cv.pyrUp(pyramid_image[i], dstsize=pyramid_image[i].shape[:2])
            lpls = cv.subtract(pyramid_image[i], expand)
            cv.imshow("lapalian_down_" + str(i), lpls)



# ----------------------------------
print("Hello to Opencv world")
src = cv.imread("F:\\pythonwork\\opencv\\1.jpg")  # 地址
cv.namedWindow("input image", cv.WINDOW_AUTOSIZE) # 窗口设置名称，自由尺寸

t1 = cv.getTickCount()
pyramid_demo(src)
lapalian_demo(src)
t2 = cv.getTickCount()
print((t2 - t1)/cv.getTickFrequency() * 1000)
cv.waitKey(3000)

cv.destroyAllWindows()