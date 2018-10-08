from aip import AipSpeech



def gen_voice(words):
    APP_ID = '10989511'
    API_KEY = 'LKjcileZ5ib4bxSGHwcNQNt1'
    SECRET_KEY = 'Q4pbFUMbHuS3IMhFl0qXQisgQuGbqgh9'
    client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)
    result  = client.synthesis(words,'zh', 1, {'vol': 3,})

    # 识别正确返回语音二进制 错误则返回dict 参照下面错误码
    if not isinstance(result, dict):
        with open('re_voice.amr', 'wb') as f:
            f.write(result)
#
# words = '陈德任，你好'
# gen_voice(words)

import itchat
# import全部消息类型
from itchat.content import *
from aip import AipOcr
import re

# 定义常量
# 识别图像中的文字

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
# @itchat.msg_register([TEXT, MAP, CARD, NOTE, SHARING])
# def text_reply(msg):
#     # 微信里，每个用户和群聊，都使用很长的ID来区分
#     # msg['FromUserName']就是发送者的ID
#     # 将消息的类型和文本内容返回给发送者
#     itchat.search_friends(nickName=r'小y')
#     print(msg['Type'])
#     itchat.send('@%s@%s' % ('Attatchment' if msg['Type'] == 'Text' else 'fil', 'audio.mp3'), msg['FromUserName'])
#     print("sucess")


# 处理多媒体类消息
# 包括图片、录音、文件、视频
# @itchat.msg_register([PICTURE, RECORDING, ATTACHMENT, VIDEO])
# def download_files(msg):
#     # msg['Text']是一个文件下载函数
#     # 传入文件名，将文件下载下来
#     msg['Text'](msg['FileName'])
#     # 高精度版  basicAccurate(self, image, options=None):
#     itchat.search_friends(nickName=r'python测试')
#     itchat.send_image('F:\pythonwork\weixin_chat\wechat\wechat_all_function/audio.mp3', toUserName='小y')
#     print('sucess')

# @itchat.msg_register([PICTURE, RECORDING, ATTACHMENT, VIDEO])
# def download_files(msg):
#     msg.download(msg.fileName)
#     print(msg['Type'])
#     # itchat.send('@%s@%s' % ('img' if msg['Type'] == 'Picture' else 'fil', msg['FileName']),msg['FromUserName'])
#
#     itchat.send('@%s@%s' % ('img' if msg['Type'] == 'Picture' else 'fil', 'audio.mp3'),msg['FromUserName'])
#     return '%s received' % msg['Type']

@itchat.msg_register(FRIENDS)
@itchat.msg_register([TEXT, PICTURE, RECORDING, ATTACHMENT, VIDEO])
def download_files(msg):
    msg.download(msg.fileName)
    print(msg['Text'])
    gen_voice(msg['Text'])
    # itchat.send('@%s@%s' % ('img' if msg['Type'] == 'Picture' else 'fil', msg['FileName']),msg['FromUserName'])
    itchat.send('@%s@%s' % ('fil', 're_voice.amr'), msg['FromUserName'])
    return '%s received' % msg['Type']
# 在auto_login()里面提供一个True，即hotReload=True
# 即可保留登陆状态
# 即使程序关闭，一定时间内重新开启也可以不用重新扫码
itchat.auto_login(True)
itchat.run()