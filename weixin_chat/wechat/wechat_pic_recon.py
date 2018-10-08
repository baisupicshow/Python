# -*- coding: UTF-8 -*-
import string
from aip import AipFace
import re
# 定义常量
APP_ID = 'xxxxxxxxxxx'
API_KEY = 'xxxxxxxxxxxxxxx'
SECRET_KEY = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxx'

# 初始化AipFace对象
aipFace = AipFace(APP_ID, API_KEY, SECRET_KEY)

# 读取图片
filePath = "1.jpg"


def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

    # 定义参数变量


# options = {
#     'max_face_num': 1,
#     'face_fields': "age",
# }
options = {
    'max_face_num': 1,
    'face_fields': "age,beauty,expression,faceshape,gender,glasses,race,type",
}
# 调用人脸属性检测接口
result = aipFace.detect(get_file_content(filePath), options)

print(result)
# print(type(result))
a = result.get('result')
print(a)
a = str(a)
b = a.split(':')
print(b)
if b:
    print('bucunzai')
for i in range(50):
    print(i,'\t',b[i])

age = b[11]
beauty = b[12]

race =b[30]
gender = b[26]
age = age.split(',')
gender = gender.split(',')
beauty = beauty.split(',')

race = race.split(',')
#年龄
print("年龄：",age[0])
#性别
if gender[0] == (" 'male'"):
   pgender = '男'
else:
   pgender = '女'
print("性别：",pgender)
#人种
if race[0] == " 'yellow'":
    race = '黄种人'
elif race[0] == " 'white'":
    race = '白种人'
else:
    race = '黑人'
print("人种：",race)


#魅力值判断
print(beauty)
# beauty = ord(beauty[0].strip())
beauty = beauty[0]
numbe = beauty[1:4]
numbe = float(numbe)

beauty = beauty[1:6]
print("魅力：",beauty,"（0-100）")
#是否戴眼镜0=no,1=yes
glass = b [28]
print(glass)
if glass[1] == str(0):
    gla = '不戴眼镜'
else:
    gla = '戴眼镜'
print(gla)
#表情 0 = no smile 1=smile，2=laugh
experssion = b[13]
print(experssion[1])
if experssion[1] == str(0):
    expre = '冷漠'
elif experssion[1] == str(1):
    expre = '微笑'
else:
    expre = '大笑'

print('表情：',expre)


#脸型
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
face_list = [face_squ,face_tra,face_ova,face_hea,face_rou]
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

reliable = b[6]
reliable = reliable[1:8]
reliable = float(reliable)
if reliable <0.6:
    print('你可别骗本机器人哦，这可能不是一张真实的脸')
print(reliable)
print(face_list)
print("脸型：",face_type)
