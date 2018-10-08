import requests
import itchat  # 这是一个用于微信回复的库
import time
KEY = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'  # 这个是图灵机器人，建议自己注册一个

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

# 装饰器
# @itchat.msg_register(itchat.content.TEXT, isGroupChat=True)   #在群里说话
@itchat.msg_register(itchat.content.TEXT, isFriendChat=True,isGroupChat=True) #跟跟好友对话

# @itchat.msg_register(itchat.content.TEXT)
def tuling_reply(msg):
    # 为了保证在图灵Key出现问题的时候仍旧可以回复，这里设置一个默认回复
    defaultReply = '收到 '
    time.sleep(0.5)
    # print(msg["Text"][0:4])
    print(msg["Text"])
    # nick_name = msg["User"].get("NickName")
    # if nick_name == "小y":  #好友名字或者群名称
    # nick_name = msg["User"].get("NickName")#昵称
    nick_name = msg["User"].get("NickName")#备注
    # if nick_name == "小y" or  (msg.isAt):  #好友名字或者群名称
    if nick_name == "小y" : #好友名字或者群名称
    # 如果图灵Key出现问题，那么reply将会是None
        reply = get_response(msg['Text'])
        # reply = reply + '\n<自动回复>'
        # a or b的意思是，如果a有内容，那么返回a，否则返回b
        return reply or defaultReply


# 为了让修改程序不用多次扫码,使用热启动
itchat.auto_login(hotReload=True)
itchat.run()
