import requests
from qqbot import _bot as bot
from qqbot import QQBotSlot as qqbotslot, RunBot
bot.Login(['-q', '1431077852'])

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



# @itchat.msg_register(itchat.content.TEXT)
def tuling_reply(bot, contact, member, content):
    # 为了保证在图灵Key出现问题的时候仍旧可以回复，这里设置一个默认回复
    # print(msg["Text"][0:4])
    print(content)
    b1 = bot.List('buddy','任')
    b = b1[0]
    reply = get_response(content)
    reply = reply + '\n<自动回复>'
    bot.SendTo(b,reply)

if __name__ == '__main__':
    RunBot()
    tuling_reply()