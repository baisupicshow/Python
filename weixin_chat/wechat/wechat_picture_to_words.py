import itchat
# import全部消息类型
from itchat.content import *
from aip import  AipOcr
import re
# 定义常量
#识别图像中的文字
APP_ID = 	'xxxxxxxxxxxx'
API_KEY = 'xxxxxxxxxxxxx'
SECRET_KEY = 'xxxxxxxxxxxxxxxxxxxxxxxxx'
# 初始化AipFace对象
'''
  client = AipOcr(APP_ID, API_KEY, SECRET_KEY)
            
i = open(r'F:\百度aip\1.jpg','rb')
img = i.read()
# message = client.basicGeneral(img)
message = client.basicAccurate(img,options=None)
# print(message)
#高精度版  basicAccurate(self, image, options=None):
for i in message.get('words_result'):
 print(i.get('words'))
'''

# 处理文本类消息
# 包括文本、位置、名片、通知、分享
@itchat.msg_register([TEXT, MAP, CARD, NOTE, SHARING])
def text_reply(msg):
    # 微信里，每个用户和群聊，都使用很长的ID来区分
    # msg['FromUserName']就是发送者的ID
    # 将消息的类型和文本内容返回给发送者
    itchat.send('%s: %s' % (msg['Type'], msg['Text']), msg['FromUserName'])

# 处理多媒体类消息
# 包括图片、录音、文件、视频
@itchat.msg_register([PICTURE, RECORDING, ATTACHMENT, VIDEO])
def download_files(msg):
    # msg['Text']是一个文件下载函数
    # 传入文件名，将文件下载下来
    msg['Text'](msg['FileName'])
    client = AipOcr(APP_ID, API_KEY, SECRET_KEY)
    print(msg['FileName'])
    i = open(msg['FileName'], 'rb')
    img = i.read()
    # message = client.basicGeneral(img)
    message = client.basicAccurate(img, options=None)
    # print(message)
    # 高精度版  basicAccurate(self, image, options=None):
    a = ''
    for i in message.get('words_result'):
        print(i.get('words'))
        a += i.get('words') + '\n'
    return a



# 在auto_login()里面提供一个True，即hotReload=True
# 即可保留登陆状态
# 即使程序关闭，一定时间内重新开启也可以不用重新扫码
itchat.auto_login(True)
itchat.run()