# 加载和保存图片
import cv2 as cv

def get_image_info(image):
    print(type(image))
    print(image.shape)
    print(image.size)
    print(image.dtype)

src = cv.imread("F:\\pythonwork\\opencv\\1.jpg")  # 地址
cv.namedWindow("input image", cv.WINDOW_AUTOSIZE) # 窗口设置名称，自由尺寸
cv.imshow("input image",src) # 打开图片
get_image_info(src)
cv.waitKey(0) # 等待
cv.destroyAllWindows() # 关闭