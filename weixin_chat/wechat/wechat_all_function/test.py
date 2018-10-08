import itchat
# import全部消息类型
from itchat.content import *
from aip import AipOcr
from aip import AipImageClassify
from urllib import parse
import re
from aip import AipFace
import time
# 定义常量
#chat
import requests
KEY = 'f9237861bc284488b37b4727b2be18f9'  # 这个是图灵机器人，建议自己注册一个
# 向api发送请求，不要改动
def get_response(msg):
    apiUrl = 'http://www.tuling123.com/openapi/api'
    data = {
        'key': KEY,
        'info': msg,
        'userid': 'pth-robot',
    }
    try:
        r = requests.post(apiUrl, data=data).json()
        return r.get('text')
    except:
        return

# get picture words
def pic_words(img):
    # 识别图像中的文字
    APP_ID = 'd6c58a8883714fc789e10f3920861900'
    API_KEY = '39fb27209e1f4fcba43d4b1e48488b4c'
    SECRET_KEY = '5620f09a14604f959ee15411cdc07105'
    # 初始化AipFace对象
    client = AipOcr(APP_ID, API_KEY, SECRET_KEY)
    message = client.basicAccurate(img, options=None)
    return message

#recongnize plant
def plant_rec(img):
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
    result = aipPlant.plantDetect(img,options=None)
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
    return read_data

# recognize cars
def car_rec(img):
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
    result = aipPlant.carDetect(img, options=None)
    a = result.get('result')
    a = str(a)
    b = a.split(':')
    k = '可能植物：'
    for i in range(1, len(b)):
        b[i] = b[i].replace(',', '')
        b[i] = b[i].replace('[', '')
        b[i] = b[i].replace(']', '')
        b[i] = b[i].replace("'name'", '')
        b[i] = b[i].replace("'score'", '')
        b[i] = b[i].replace("'", '')
        b[i] = b[i].replace("{", '')
        b[i] = b[i].replace("}", '')
        b[i] = b[i].replace("year", '')
        k = k + b[i]
        k = k + '\n'
    # print(k)
    plant_list = k.split('\n')
    plant_out = '汽车名称' + '可能性'.rjust(30 - len('植物名称'.encode('utf-8'))) + '\n'
    for i in range(1, len(plant_list) - 2, 3):
        plant_out = plant_out + plant_list[i]
        # plant_list[i+1] = plant_list[i+1].strip()
        # print()
        plant_out = plant_out + plant_list[i + 2].rjust(30 - len(plant_list[i].encode('utf-8')))
        plant_out = plant_out + '\n'
    # print(plant_list[2])
    plant_out = plant_out + 'https://baike.baidu.com/item/' + parse.quote(plant_list[1].strip())
    read_data = plant_out
    print(plant_out)
    return read_data

# face
def face_rec(img):
    APP_ID = '11029448'
    API_KEY = 'Bkq4j0m8CmjbBkdDadt1nnPW'
    SECRET_KEY = 'oRcMQVcly2GdTfVbHzKNX5h6hrQo1gZE'
    # 初始化AipFace对象
    aipFace = AipFace(APP_ID, API_KEY, SECRET_KEY)
    # 读取图片

    # 定义参数变量
    options = {
        'max_face_num': 1,
        'face_fields': "age,beauty,expression,faceshape,gender,glasses,type,race",
    }
    # 调用人脸属性检测接口
    result = aipFace.detect(img, options)
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
        print(reliable)
        if reliable[1] != str(1):
            reliable = reliable[1:8]
            # print(reliable)
            reliable = float(reliable)
            if reliable < 0.9:
                read_data = '你可别骗本机器人哦，这可能不是一张真实的脸'
            print(read_data)
            # return(age[0],pgender,race,beauty,expre,face_type,gla)
    else:
        read_data = '你可别骗本机器人哦，这不是一张人脸！'
    print(reliable)
    return read_data

#消息返回类型全局变量
re_text = 1
# 处理文本类消息
# 包括文本、位置、名片、通知、分享
@itchat.msg_register([TEXT, MAP, CARD, NOTE, SHARING],isGroupChat=True)
def text_reply(msg):
    # 微信里，每个用户和群聊，都使用很长的ID来区分
    # msg['FromUserName']就是发送者的ID
    # 将消息的类型和文本内容返回给发送者
    global re_text
    time.sleep(0.1)
    print(msg["Text"])
    nick_name = msg["User"].get("NickName")
    if nick_name == "python测试":
        if msg["Text"] == "聊天" or msg['Text'] == '1':
            re_text = 1
            return "我们来聊天吧"
        if msg["Text"] == "植物识别" or msg['Text'] == '2':
            re_text = 2
            return "请发送一张植物图片"
        if msg["Text"] == "汽车识别" or msg['Text'] == '3':
            re_text = 3
            return "请发送一张汽车图片"
        if msg['Text'] == "识字" or msg['Text'] == '4':
            re_text = 4
            return "请发送一张有文字（中英文）的图片"
        if msg['Text'] == "人脸" or msg['Text'] == '5':
            re_text = 5
            return "请发送一张人脸图片"
        if msg['Text'] == "你好"or msg['Text'] =="功能":
            return ("你好，我能自动回复功能有：\n" \
                   "1.聊天\n" \
                   "2.植物识别\n" \
                   "3.汽车识别\n" \
                   "4.识字\n" \
                   "5.人脸\n"  
                   "发送以上数字或者文字实现不同功能")
        print(re_text)
        if re_text == 1 :
            b = get_response(msg['Text'])
            return b

# 处理多媒体类消息
# 包括图片、录音、文件、视频
@itchat.msg_register([PICTURE, RECORDING, ATTACHMENT, VIDEO],isGroupChat=True)
def download_files(msg):
    # msg['Text']是一个文件下载函数
    # 传入文件名，将文件下载下来
    global re_text
    msg['Text'](msg['FileName'])
    print(msg['FileName'])
    i = open(msg['FileName'], 'rb')
    img = i.read()
    time.sleep(1)
    a = ''
    nick_name = msg["User"].get("NickName")
    if nick_name == "python测试":
        if re_text == 2:
            message = plant_rec(img)
            a = message
        if re_text == 3:
            message = car_rec(img)
            a = message
        if re_text == 4:
            message = pic_words(img)
            for i in message.get('words_result'):
             print(i.get('words'))
             a += i.get('words') + '\n'
        if re_text == 5:
            message = face_rec(img)
            a = message
    # message = client.basicGeneral(img)
    # print(message)
    # 高精度版  basicAccurate(self, image, options=None):


    return a


# 在auto_login()里面提供一个True，即hotReload=True
# 即可保留登陆状态
# 即使程序关闭，一定时间内重新开启也可以不用重新扫码
itchat.auto_login(True)
itchat.run()