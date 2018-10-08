#coding = utf-8

import itchat

#登录微信
itchat.auto_login(hotReload=True)
#发消息 获取好友列表，给特定的好友发消息,同时可以更新列表
# friends_list = itchat.get_friends(update=True)
# print(friends_list[0]["UserName"])
frs = itchat.search_friends(nickName="pythons")
print(frs[0])
# # print(frs)
# # itchat.send("代码测试，请勿回复",toUserName=frs[0]["UserName"])
# # itchat.send("1.jpg",toUserName=frs[0]["UserName"])
# itchat.send(msg="你好",toUserName="pythons")
# itchat.send("@img@%s" % '1.jpg',toUserName=None)
# itchat.send("你好",toUserName=frs[0]["UserName"])
itchat.send("@img@%s" % '1.jpg',toUserName=frs[0]["UserName"])