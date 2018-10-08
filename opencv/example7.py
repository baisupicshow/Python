# 高斯模糊
import cv2 as cv
import numpy as np

def clamp(pv):
    if pv > 255:
        return 255
    if pv < 0:
        return 0
    else:
        return pv

def gaussian__noise(image):
    h, w, c = image.shape
    for row  in range(h):
        for col in range(w):
            s = np.random.normal(0, 20, 3)
            b = image[row, col, 0] # blue
            g = image[row, col, 1] # green
            r = image[row, col, 2] # red
            image[row, col, 0] = clamp(b + s[0])
            image[row, col, 1] = clamp(g + s[1])
            image[row, col, 2] = clamp(r + s[2])
    cv.imshow("gaussian_noise_img",image)


src = cv.imread("F:\\pythonwork\\opencv\\1.jpg")  # 地址
cv.namedWindow("input image", cv.WINDOW_AUTOSIZE) # 窗口设置名称，自由尺寸
cv.imshow("input image",src) # 打开图片
t1 = cv.getTickCount()
gaussian__noise(src)
t2 = cv.getTickCount()
print((t2 - t1)/cv.getTickFrequency() * 1000)
dst = cv.GaussianBlur(src, (0, 0), 1)
cv.imshow("1gaussion_blur", dst) # 调用高斯工具
cv.waitKey(3000)