from aip import  AipOcr
import re
# 定义常量
#识别图像中的文字
APP_ID = 	'xxxxxxxxxxxx'
API_KEY = 'xxxxxxxxxxxxxxxx'
SECRET_KEY = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
# 初始化AipFace对象
client = AipOcr(APP_ID, API_KEY, SECRET_KEY)

i = open(r'F:\百度aip\1.jpg','rb')
img = i.read()
# message = client.basicGeneral(img)
message = client.basicAccurate(img,options=None)
# print(message)
#高精度版  basicAccurate(self, image, options=None):
for i in message.get('words_result'):
     print(i.get('words'))