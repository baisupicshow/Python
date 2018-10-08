# from qqbot import QQBotSlot as qqbotslot,RunBot
# class MyQQBot(QQBot):
#     def onPollComplete(self, msgType, from_uin, buddy_uin, message):
#         if message == '-hello':
#             self.send(msgType, from_uin, '你好，我是QQ机器人')
#         elif message == '-stop':
#             self.stopped = True
#             self.send(msgType, from_uin, 'QQ机器人已关闭')
#
# myqqbot = MyQQBot()
# myqqbot.Login()
# myqqbot.PollForever()

from qqbot import QQBotSlot as qqbotslot, RunBot


@qqbotslot
def onQQMessage(bot, contact, member, content):
    if content == '-hello':

        bot.SendTo(contact, '你好，我是QQ机器人')
        print(content)
        bot.SendTo(contact, '你好，我是QQ机器人')
    elif content == '-stop':

        bot.SendTo(contact, 'QQ机器人已关闭')

        bot.Stop()


if __name__ == '__main__':
    RunBot()
