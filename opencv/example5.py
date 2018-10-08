import cv2 as cv
import numpy as np

def fill_color_demo(image):
    copyIma = image.copy()
    h, w = image.shape[:2]
    mask = np.zeros([h+2, w+2],np.uint8)
    cv.floodFill(copyIma, mask, (30, 30), (0,255, 255), (100,100, 100), (50, 50, 50 ), cv.FLOODFILL_FIXED_RANGE)
    cv.imshow("fill_color_demo", copyIma)

def fill_cbinary():
    image = np.zeros([400, 400, 3], np.uint8)
    image[100:300, 100:300, :] = 120
    cv.imshow("Fill_binary",image)

    mask = np.ones([402, 402, 1], np.uint8)
    mask[101:301, 101:301] = 0
    cv.floodFill(image, mask, (200, 200), (100, 2, 255), cv.FLOODFILL_MASK_ONLY)
    cv.imshow("mask_binary",image)

'''
# ROI区
src = cv.imread("F:\\pythonwork\\opencv\\1.jpg")  # 地址
cv.namedWindow("input image", cv.WINDOW_AUTOSIZE) # 窗口设置名称，自由尺寸
cv.imshow("input image",src) # 打开图片
face = src[20:200,50:300] # 选择脸部区域
cv.imshow("face",face)
# 改变选择区域为灰度图
gray = cv.cvtColor(face,cv.COLOR_BGR2GRAY)
backface = cv.cvtColor(gray,cv.COLOR_GRAY2BGR)
src[20:200,50:300] = backface
'''
src = cv.imread("F:\\pythonwork\\opencv\\1.jpg")  # 地址
cv.namedWindow("input image", cv.WINDOW_AUTOSIZE) # 窗口设置名称，自由尺寸
cv.imshow("input image",src) # 打开图片
cv.imshow("chage",src)

fill_color_demo(src)
fill_cbinary()
cv.waitKey(3000)