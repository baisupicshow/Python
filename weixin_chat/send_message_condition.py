import itchat
import time
from aip import  AipOcr
from PIL import ImageGrab
import pythoncom
import pyHook





# 全局变量
global users
#识别图像中的文字(百度ai——ocr)
APP_ID = 	'xxxxxxxxxxxxxxxxxxxxxxxxx'
API_KEY = 'xxxxxxxxxxxxxxxxxxxx'
SECRET_KEY = 'xxxxxxxxxxxxxxxxxxxxxxxxxx'
def get_words(img):
    client = AipOcr(APP_ID, API_KEY, SECRET_KEY)
    message = client.basicAccurate(img, options=None)
    a = ''
    for i in message.get('words_result'):
        print(i.get('words'))
        a += i.get('words') + '\n'
    return a



def onMouse_rightdown(event):
    # 监听鼠标左键按下事件
    global users
    print( "left DOWN DOWN" )
    im = ImageGrab.grab((300,300,1000,1000))
    im.save("1.jpg")
    i = open("1.jpg", 'rb')
    img = i.read()
    itchat.send(str(get_words(img)),toUserName=users[0]['UserName'])#发消息给好友
    itchat.send_image('1.jpg',toUserName=users[0]['UserName'])
    itchat.send('hello','filehelper') #发消息给自己微信
    time.sleep(1)
    return True


def main():
    hm = pyHook.HookManager()
    hm.MouseRightDown = onMouse_rightdown
    hm.HookMouse()
    # 进入循环，如不手动关闭，程序将一直处于监听状态
    pythoncom.PumpMessages()
if __name__ == "__main__":
    itchat.auto_login(hotReload=True)
    users = itchat.search_friends(name=U'小y')  # 好友昵称
    main()



