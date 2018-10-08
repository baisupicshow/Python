# import urllib,urllib2
# import sys
# import json
#
# reload(sys)
# sys.setdefaultencoding('utf-8')
#
# API_KEY = 'bc192acc72f2768b211c193*****'
# raw_TULINURL = "http://www.tuling123.com/openapi/api?key=%s&info=" % API_KEY
#
# def result():
#     for i in range(1,100):
#         queryStr = raw_input("我:".decode('utf-8'))
#         TULINURL = "%s%s" % (raw_TULINURL,urllib2.quote(queryStr))
#         req = urllib2.Request(url=TULINURL)
#         result = urllib2.urlopen(req).read()
#         hjson=json.loads(result)
#         length=len(hjson.keys())
#         content=hjson['text']
#
#         if length==3:
#             return 'robots:' +content+hjson['url']
#         elif length==2:
#             return 'robots:' +content
#
# if __name__=='__main__':
#     print "你好，请输入内容:".decode('utf-8')
#     contents=result()
#     print contents
'''''
Created by swh on 2017.09.18
'''
# 图灵机器人的返回内容有文本、图片、地址
import requests
from json import loads


class LoginTic(object):
    def __init__(self):
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36"
        }

        self.key = 'f9237861bc284488b37b4727b2be18f9'
        # 创建一个网络请求session实现登录验证
        self.session = requests.session()

    def talkWithTuling(self, text):
        url = 'http://www.tuling123.com/openapi/api'
        data = {
            'key': self.key,  # key
            'info': text,  # 发给图灵的内容
            'userid': '123456swh'  # 用户id,自己设置1-32的字母和数字组合
        }
        response = requests.post(url=url, headers=self.headers, data=data)
        return response.text


if __name__ == '__main__':
    ll = LoginTic()
    userName = ('斗图')
    # cont = ll.talkWithTuling('你好')
    cont = ll.talkWithTuling(userName)
    # print(cont["url"])
    dd = loads(cont)
    print(dd['url'])
    # print(dd)
    if dd['code'] == 100000:
        # 返回的是文本
        print
        '-' * 10
        print
        dd['text']
    elif dd['code'] == 200000:
        # '链接累的内容'
        print
        dd['text']
        print
        dd['url']
    elif dd['code'] == 302000:
        # 新闻类的内容
        print
        dd['text']
        print
        len(dd['list'])

    elif dd['code'] == 308000:
        # 菜谱类的内容
        pass

    elif dd['code'] == 313000:
        # 儿歌类的
        pass

    elif dd['code'] == 314000:
        # 儿童诗词类的
        pass


