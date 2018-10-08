# 人脸检测

import cv2 as cv
import numpy as np

def face_detect_demo(image):
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    face_detector = cv.CascadeClassifier('F:\pythonwork\opencv\haarcascade_frontalface_alt_tree.xml')
    faces = face_detector.detectMultiScale(gray, 1.2, 0)
    for x, y, w, h in faces:
        cv.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)
    cv.imshow("result", image)


print("Hello to Opencv world")
src = cv.imread("F:\\pythonwork\\opencv\\manyface2.jpg")  # 地址

# cv.namedWindow("input image", cv.WINDOW_AUTOSIZE) # 窗口设置名称，自由尺寸
cv.imshow("origin", src)
t1 = cv.getTickCount()

face_detect_demo(src)

t2 = cv.getTickCount()
print((t2 - t1) / cv.getTickFrequency() * 1000)
cv.waitKey(4000)

cv.destroyAllWindows()
