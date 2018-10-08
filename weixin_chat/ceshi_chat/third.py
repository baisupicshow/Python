#conding=utf-8
#回复好友
import itchat
from itchat.content import TEXT

#装饰器，确定只回复好友
@itchat.msg_register([TEXT,], isGroupChat=True)

def print_content(msg):
    print(msg["Text"])
    nick_name = msg["User"].get("NickName")
    print(nick_name)
    if nick_name == "python测试":
        return '你好啊'

if __name__ == "__main__":
    try:
        itchat.auto_login(hotReload=True)
        itchat.run()
    except Exception as e:
        print(e)
