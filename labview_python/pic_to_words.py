from aip import AipOcr  # baidu-aip
import sys
def pic_words(img):
    # 识别图像中的文字
    APP_ID = 'xxxxxxxxxxxxxxxxx'   # 从百度AI注册获取，免费
    API_KEY = 'xxxxxxxxxxxxxxxxxxxxxxxx'
    SECRET_KEY = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxx'
    # 初始化AipFace对象
    client = AipOcr(APP_ID, API_KEY, SECRET_KEY)
    img = get_file_content(img)
    message = client.basicAccurate(img, options=None)
    a = ''
    for i in message.get('words_result'):
        print(i.get('words'))
        a += i.get('words') + '\n'
    return a

def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

message = pic_words(sys.argv[1])
print(pic_words(message))