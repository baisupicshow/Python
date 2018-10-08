from qqbot import QQBotSlot as qqbotslot, RunBot
from qqbot import _bot as bot
bot.Login(['-q', '1431077852'])


def onQQMessage(bot, contact, member, content):
    if content != None:
        bot.SendTo(contact, '你好，我是QQ机器人')
        print(content)


if __name__ == '__main__':
    RunBot()
