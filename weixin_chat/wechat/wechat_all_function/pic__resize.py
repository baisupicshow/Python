# coding=utf-8
import time
time1 = time.time()
import cv2
from PIL import Image
image=cv2.imread(r"F:\pythonwork\weixin_chat\wechat\IMG_20170402_111340.jpg")
print(image.shape)
print(image.size)
res = cv2.resize(image, (2080,1560), interpolation=cv2.INTER_AREA)
# cv2.imshow('image', image)
# cv2.imshow('resize', res)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
cv2.imwrite(r"F:\pythonwork\weixin_chat\wechat\wechat_all_function\1.jpg",res)
time2=time.time()
print (u'总共耗时：' + str(time2 - time1) + 's')