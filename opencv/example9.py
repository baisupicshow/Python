from matplotlib import pyplot as plt
import cv2 as cv
import numpy as np

def plot_demo(image):
    plt.hist(image.ravel(), 256, [0, 256])
    plt.show("直方图")

# 3通道直方图
def image_hist(image):
    color = ("blue", "green", "red")
    for i, color in enumerate(color):
        hist = cv.calcHist([image], [i], None, [256], [0, 256])
        plt.plot(hist, color=color)
        plt.xlim([0, 256])
    plt.show()


print("OPENCV TEST")

src = cv.imread("F:\\C++\\test\\3432.png")  # 地址
cv.namedWindow("input image", cv.WINDOW_AUTOSIZE) # 窗口设置名称，自由尺寸
cv.imshow("input image",src) # 打开图片
t1 = cv.getTickCount()
plot_demo(src)
image_hist(src)
t2 = cv.getTickCount()
print((t2 - t1)/cv.getTickFrequency() * 1000)
cv.waitKey(3000)


