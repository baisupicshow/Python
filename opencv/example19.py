# 圆检测
# 发现可能的圆心


'''

cv2.HoughCircles(image, method, dp, minDist[, circles[, param1[, param2[, minRadius[, maxRadius]]]]]) → circles
参数说明:
image- 8位，单通道，灰度输入图像。
circles- 找到的圆的输出向量。每个向量被编码为3元素的浮点向量 （x，y，半径）。
circle_storage - 在C函数中，这是一个将包含找到的圆的输出序列的内存存储。
method- 使用检测方法。目前，唯一实现的方法是 CV_HOUGH_GRADIENT，基本上是 21HT，在[Yuen90]中有描述 。
dp - 累加器分辨率与图像分辨率的反比。例如，如果 dp = 1，则累加器具有与输入图像相同的分辨率。如果 dp = 2，则累加器的宽度和高度都是一半。
minDist -检测到的圆的中心之间的最小距离。如果参数太小，除了真正的参数外，可能会错误地检测到多个邻居圈。如果太大，可能会错过一些圈子。
param1 - 第一个方法特定的参数。在CV_HOUGH_GRADIENT的情况下， 两个传递给Canny（）边缘检测器的阈值较高（较小的两个小于两倍）。
param2 - 第二种方法参数。在CV_HOUGH_GRADIENT的情况下
，它是检测阶段的圆心的累加器阈值。越小，可能会检测到越多的虚假圈子。首先返回对应于较大累加器值的圈子。
minRadius -最小圆半径。
maxRadius - 最大圆半径。
'''
import cv2 as cv
import numpy as np

def circle_detection(image):
    dst = cv.pyrMeanShiftFiltering(image, 6, 20)
    gray = cv.cvtColor(dst, cv.COLOR_BGR2GRAY)
    cv.imshow("gary",gray)
    circles = cv.HoughCircles(gray, cv.HOUGH_GRADIENT, 1, 100, param1=50, param2=40,minRadius=1, maxRadius=100)
    circles = np.uint16(np.around(circles))
    print(circles)
    # 1是两个圆的最小距离，最后设为0表示不定义
    for i in circles[0, :, :]:
        cv.circle(image, (i[0], i[1]), i[2], (0, 0, 255), 2)
        cv.circle(image, (i[0], i[1]), 2, (255, 0, 0), 2)
    cv.imshow("circles", image)











# ----------------------------------
print("Hello to Opencv world")
src = cv.imread("F:\\pythonwork\\opencv\\circle_test.jpg")  # 地址
# cv.namedWindow("input image", cv.WINDOW_AUTOSIZE) # 窗口设置名称，自由尺寸
# cv.imshow("origin", src)
t1 = cv.getTickCount()

circle_detection(src)

t2 = cv.getTickCount()
print((t2 - t1) / cv.getTickFrequency() * 1000)
cv.waitKey(00)

cv.destroyAllWindows()
