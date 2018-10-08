# 色彩空间
# 常见色彩空间 RGB，HSV，HIS，YCrCb，YUV
import cv2 as cv
import numpy as np

def reshpe():
    m1 = np.ones([3, 3],np.uint8)
    m2 = m1.reshape([1,9])
    print(m2)

def color_space_demo(image):
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    cv.imshow("gray",gray)
    hsv = cv.cvtColor(image, cv.COLOR_BGR2HSV)
    cv.imshow("hsv",hsv)
    yuv = cv.cvtColor(image, cv.COLOR_BGR2YUV)
    cv.imshow("yuv",yuv)
    Ycrcb = cv.cvtColor(image,cv.COLOR_RGB2YCR_CB)
    cv.imshow("Ycrcb",Ycrcb)


src = cv.imread("F:\\pythonwork\\opencv\\1.jpg")  # 地址
cv.namedWindow("input image", cv.WINDOW_AUTOSIZE) # 窗口设置名称，自由尺寸
cv.imshow("input image",src) # 打开图片

t1 = cv.getTickCount()
color_space_demo(src)
t2 = cv.getTickCount()
print("Time: %s ms" %((t2-t1)/cv.getTickFrequency()*1000))
cv.waitKey(0) # 等待
cv.destroyAllWindows() # 关闭