# 测量
# 长度、弧长、面积
# 多边形拟合，获取多边形拟合
# approx
import cv2 as cv
import numpy as np

def measure_object(image):
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    ret, binary = cv.threshold(gray, 0, 255, cv.THRESH_BINARY_INV | cv.THRESH_OTSU)
    ret, binary = cv.threshold(gray, 0, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)
    print("threshhold value: %s"%ret)
    cv.imshow("binary", binary)
    dst = cv.cvtColor(binary, cv.COLOR_GRAY2BGR)
    cv.imshow('dst',dst)
    outImage, contours, hireachy = cv.findContours(binary, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
    for i, contour in enumerate(contours):
        area = cv.contourArea(contour)
        x, y, w, h = cv.boundingRect(contour)
        rate = min(w, h) / max(w, h)
        print("rectangle rate :%s"%rate)
        mm = cv.moments(contour)
        print(type(mm))
        print(mm['m00'])
        if mm['m00'] == 0:
            mm['m00'] = 1
        cx = mm['m10'] / mm['m00']
        cy = mm['m01'] / mm['m00']
        cv.circle(image, (np.int(cx), np.int(cy)), 3, (0, 255, 255), -1)
        # cv.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)
        print('contour area: %s'%area)
        approxCurv = cv.approxPolyDP(contour, 4, True)
        print(approxCurv)
        if approxCurv.shape[0] > 10:
            cv.drawContours(dst, contours, i, (0, 255, 0), 2)
        if approxCurv.shape[0] < 10:
            cv.drawContours(dst, contours, i, (255, 255, 0), 2)
    cv.imshow("measure-contours", image)




# ----------------------------------
print("Hello to Opencv world")
src = cv.imread("F:\\pythonwork\\opencv\\numbers.jpg")  # 地址
src = cv.imread("F:\\pythonwork\\opencv\\jihe2.jpg")  # 地址
# cv.namedWindow("input image", cv.WINDOW_AUTOSIZE) # 窗口设置名称，自由尺寸
# cv.imshow("origin", src)
t1 = cv.getTickCount()

measure_object(src)

t2 = cv.getTickCount()
print((t2 - t1) / cv.getTickFrequency() * 1000)
cv.waitKey(00)

cv.destroyAllWindows()


