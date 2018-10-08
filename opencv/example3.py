import cv2 as cv
import numpy as np

def access_pixels(image):
    print(image.shape)
    height = image.shape[0]
    width = image.shape[1]
    channels = image.shape[2]
    print("width: %s height: %s channels: %s" %(width,height,channels))
    for row in range(height):
        for col in range(width):
            for c in range(channels):
                pv = image[row, col, c]
                image[row, col, c] = 255 - pv
    cv.imshow("pixels_demo",image)
def creat_image():
    img = np.zeros([400,400,3],np.uint8)
    img[:,:,0] = np.ones([400,400])*255
    cv.imshow("new_image",img)


src = cv.imread("F:\\pythonwork\\opencv\\1.jpg")  # 地址
cv.namedWindow("input image", cv.WINDOW_AUTOSIZE) # 窗口设置名称，自由尺寸
cv.imshow("input image",src) # 打开图片
creat_image()
t1 = cv.getTickCount()
access_pixels(src)
t2 = cv.getTickCount()
print("Time: %s ms" %((t2-t1)/cv.getTickFrequency()*1000))
cv.waitKey(0) # 等待
cv.destroyAllWindows() # 关闭