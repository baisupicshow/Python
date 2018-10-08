#conding=utf-8
#回复好友
import itchat
from itchat.content import TEXT

#装饰器，确定只回复好友
@itchat.msg_register([TEXT,], isFriendChat=True)

def print_content(msg):
    print(msg["Text"])
    return"你好啊"

if __name__ == "__main__":
    try:
        itchat.auto_login(hotReload=True)
        itchat.run()
    except Exception as e:
        print(e)

