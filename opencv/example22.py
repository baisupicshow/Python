# 膨胀，腐蚀

import cv2 as cv

def erode_demo(image):
    print(image.shape)
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    ret, binary = cv.threshold(gray, 0, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)
    kernel = cv.getStructuringElement(cv.MORPH_RECT, (5, 5))
    dst = cv.erode(binary, kernel)
    cv.imshow("erode", dst)

def dilate_demo(image):
    print(image.shape)
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    ret, binary = cv.threshold(gray, 0, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)
    kernel = cv.getStructuringElement(cv.MORPH_RECT, (5, 5))
    dst = cv.dilate(binary, kernel)
    cv.imshow("dilate", dst)
# ----------------------------------
print("Hello to Opencv world")
src = cv.imread("F:\\pythonwork\\opencv\\numbers.jpg")  # 地址
src = cv.imread("F:\\pythonwork\\opencv\\jihe2.jpg")  # 地址
# cv.namedWindow("input image", cv.WINDOW_AUTOSIZE) # 窗口设置名称，自由尺寸
# cv.imshow("origin", src)
t1 = cv.getTickCount()

erode_demo(src)
dilate_demo(src)

t2 = cv.getTickCount()
print((t2 - t1) / cv.getTickFrequency() * 1000)
cv.waitKey(00)

cv.destroyAllWindows()
