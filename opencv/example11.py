# 直方图比较 粗劣比较
import cv2 as cv
import numpy as np
# 巴氏距离 越大，相似度越低
# 相似度0-1
#

def creat_rgb_hist(image):
    h, w, c = image.shape
    rgbHist = np.zeros([16 * 16 * 16, 1], np.float32)
    bsize = 256 / 16
    for row in range(h):
        for col in range(w):
            b = image[row, col, 0]
            g = image[row, col, 1]
            r = image[row, col, 2]
            index = np.int(b / bsize) * 16 * 16 + np.int(g / bsize) * 16 + np.int(r / bsize)
            rgbHist[np.int(index), 0] = rgbHist[np.int(index), 0] + 1
    return rgbHist


def hist_compare(image1, image2):
    hist1 = creat_rgb_hist(image1)
    hist2 = creat_rgb_hist(image2)
    match1 = cv.compareHist(hist1, hist2, cv.HISTCMP_BHATTACHARYYA)
    match2 = cv.compareHist(hist1, hist2, cv.HISTCMP_CORREL)
    match3 = cv.compareHist(hist1, hist2, cv.HISTCMP_CHISQR)
    print("巴氏距离: %s \n 相关性: %s \n 卡方: %s "%(match1, match2, match3))


src1 = cv.imread("F:\\C++\\test\\3432.png")  # 地址
src2 = cv.imread("F:\\C++\\test\\3432.png")  # 地址

cv.namedWindow("input image", cv.WINDOW_AUTOSIZE) # 窗口设置名称，自由尺寸
cv.imshow("input image1",src1) # 打开图片
cv.imshow("input image2",src2) # 打开图片
t1 = cv.getTickCount()
hist_compare(src1, src2)
t2 = cv.getTickCount()
print((t2 - t1)/cv.getTickFrequency() * 1000)
cv.waitKey(3000)

cv.destroyAllWindows()


