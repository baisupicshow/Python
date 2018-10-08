# -*- coding: UTF-8 -*-
import string
from aip import AipFace
# 定义常量
import itchat
# import全部消息类型
from itchat.content import *
import time


def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()
def read_face(filePath):
    APP_ID = 'xxxxxxxxxxxxx'
    API_KEY = 'xxxxxxxxxxxxxxx'
    SECRET_KEY = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
    # 初始化AipFace对象
    aipFace = AipFace(APP_ID, API_KEY, SECRET_KEY)
    # 读取图片

    # 定义参数变量
    options = {
        'max_face_num': 1,
        'face_fields': "age,beauty,expression,faceshape,gender,glasses,type,race",
    }
    # 调用人脸属性检测接口
    result = aipFace.detect(get_file_content(filePath), options)
    a = result.get('result')
    # print(a)
    a = str(a)
    b = a.split(':')
    if len(b) > 2:
        age = b[11]
        beauty = b[12]
        race = b[30]
        gender = b[26]
        age = age.split(',')
        gender = gender.split(',')
        beauty = beauty.split(',')
        race = race.split(',')
        # 年龄
        # print("年龄：",age[0])
        # 性别
        reliable = b[6]
        if gender[0] == (" 'male'"):
            pgender = '男'
        else:
            pgender = '女'
        # print("性别：",pgender)
        # 人种
        if race[0] == " 'yellow'":
            race = '黄种人'
        elif race[0] == " 'white'":
            race = '白种人'
        else:
            race = '黑人'
        # print("人种：",race)
        # 魅力值判断
        # print(beauty)
        # beauty = ord(beauty[0].strip())
        beauty = beauty[0]
        numbe = beauty[1:4]
        beauty = beauty[1:6]
        # print("魅力：",beauty,"（0-100）")
        # 是否戴眼镜0=no,1=yes
        glass = b[28]
        # print(glass)
        if glass[1] == str(0):
            gla = '无'
        else:
            gla = '有'
        # print(gla)
        # 表情 0 = no smile 1=smile，2=laugh
        experssion = b[13]
        # print(experssion[1])
        if experssion[1] == str(0):
            expre = '冷漠'
        elif experssion[1] == str(1):
            expre = '微笑'
        else:
            expre = '大笑'
        # print('表情：',expre)
        # 脸型
        face_squ = b[17]
        face_tra = b[19]
        face_ova = b[21]
        face_hea = b[23]
        face_rou = b[25]
        face_squ = face_squ[0:9]
        face_tra = face_tra[0:9]
        face_ova = face_ova[0:9]
        face_hea = face_hea[0:9]
        face_rou = face_rou[0:9]
        face_list = [face_squ, face_tra, face_ova, face_hea, face_rou]
        face_type_num = face_list.index(max(face_list))
        if face_type_num == 0:
            face_type = '国字脸'
        elif face_type_num == 1:
            face_type = '三角脸'
        elif face_type_num == 2:
            face_type = '椭圆脸'
        elif face_type_num == 3:
            face_type = '心型脸'
        else:
            face_type = '圆脸'
        # print(face_list)
        # print("脸型：",face_type)
        read_data = ['年  龄：', age[0], '\n',
                     '性  别：', pgender, '\n',
                     '人  种：', race, '\n',
                     '魅力值：', beauty, '(0-100)', '\n',
                     '表  情：', expre, '\n',
                     '脸  型：', face_type, '\n',
                     '眼  镜：', gla]
        read_data = ','.join(read_data)
        read_data = read_data.replace(',', '')
        reliable = b[6]
        if reliable[1] != str(1):
            reliable = reliable[1:8]
            print(reliable)
            reliable = float(reliable)
            if reliable < 0.9:
                read_data = '你可别骗本机器人哦，这可能不是一张真实的脸'
            print(read_data)
            # return(age[0],pgender,race,beauty,expre,face_type,gla)
    else:
        read_data = '你可别骗本机器人哦，这不是一张人脸！'

    return read_data



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

