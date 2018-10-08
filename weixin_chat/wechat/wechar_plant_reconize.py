# -*- coding: UTF-8 -*-
import string
from aip import AipImageClassify
# 定义常量
import itchat
# import全部消息类型
from itchat.content import *
from urllib import parse

# plantDetect
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()
def read_face(filePath):
    APP_ID = '11173506'
    API_KEY = 'pwcq1rBuPvGbrOi8ORqGUKKp'
    SECRET_KEY = 'SHguMaeswBLDOrKSbGyGtjfyasLt3kQo'
    # 初始化AipFace对象
    aipPlant = AipImageClassify(APP_ID, API_KEY, SECRET_KEY)
    # 读取图片

    # 定义参数变量
    options = {
        'max_face_num': 1,
        'face_fields': "age,beauty,expression,faceshape,gender,glasses,type,race",
    }
    result = aipPlant.plantDetect(get_file_content(filePath),options=None)
    a = result.get('result')
    a = str(a)
    b = a.split(':')
    k = '可能植物：'
    for i in range(0,len(b)):
        b[i] = b[i].replace(',','')
        b[i] =  b[i].replace('[','')
        b[i] =  b[i].replace(']','')
        b[i] =  b[i].replace("'name'",'')
        b[i] =  b[i].replace("'score'",'')
        b[i] =  b[i].replace("'",'')
        b[i] =  b[i].replace("{",'')
        b[i] =  b[i].replace("}",'')

        k = k + b[i]
        k = k + '\n'
    # print(k)
    plant_list = k.split('\n')
    plant_out = '植物名称' + '可能性'.rjust(30 - len('植物名称'.encode('utf-8'))) + '\n'
    for i in range(1,len(plant_list)-1,2):
        plant_out = plant_out + plant_list[i+1]
        # plant_list[i+1] = plant_list[i+1].strip()
        # print()
        plant_out = plant_out + plant_list[i].rjust(35 - len(plant_list[i+1].encode('utf-8')))
        plant_out = plant_out + '\n'
    # print(plant_list[2])
    plant_out = plant_out + 'https://baike.baidu.com/item/' + parse.quote(plant_list[2].strip())
    read_data = plant_out
    print(plant_out)
    return read_data


# https://baike.baidu.com/item/%E7%B4%AB%E4%BA%91%E8%8B%B1/758653?fr=aladdin
# 处理多媒体类消息
# 包括图片、录音、文件、视频
# @itchat.msg_register([PICTURE, RECORDING, ATTACHMENT, VIDEO],isGroupChat=True)
@itchat.msg_register([PICTURE, RECORDING, ATTACHMENT, VIDEO],isFriendChat=True)
def download_files(msg):
    # msg['Text']是一个文件下载函数
    # 传入文件名，将文件下载下来
    msg['Text'](msg['FileName'])
    print(msg['FileName'])
    nick_name = msg["User"].get("NickName")
    if nick_name == "小y":  #好友名字或者群名称
    # 如果图灵Key出现问题，那么reply将会是None
        return read_face(msg['FileName'])
        # a or b的意思是，如果a有内容，那么返回a，否则返回b


# 在auto_login()里面提供一个True，即hotReload=True
# 即可保留登陆状态
# 即使程序关闭，一定时间内重新开启也可以不用重新扫码
itchat.auto_login(True)
itchat.run()

