# 超大图像二值化

import cv2 as cv
import numpy as np

def big_image_binary(image):
    print(image.shape)
    cw = 256
    ch = 256
    h, w = image.shape[:2]
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    for row in range(0, h, ch):
        for col in range(0, w, cw):
            roi = gray[row: row + ch, col: cw + col]
            dst = cv.adaptiveThreshold(roi, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 127, 2)
            gray[row:row + ch, col:cw + col] = dst
            print(np.std(dst), np.mean(dst))
    cv.imwrite("F:\\pythonwork\\opencv\\w2.jpg", gray)


# ----------------------------------
print("Hello to Opencv world")
src = cv.imread("F:\\pythonwork\\opencv\\wallhaven-674962.jpg")  # 地址
cv.namedWindow("input image", cv.WINDOW_AUTOSIZE) # 窗口设置名称，自由尺寸

t1 = cv.getTickCount()
big_image_binary(src)
t2 = cv.getTickCount()
print((t2 - t1)/cv.getTickFrequency() * 1000)
cv.waitKey(3000)

cv.destroyAllWindows()
