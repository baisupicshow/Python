#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
import itertools
import urllib
import requests
import os
import re
import sys
from multiprocessing import Pool
import time




str_table = {
    '_z2C$q': ':',
    '_z&e3B': '.',
    'AzdH3F': '/'
}

char_table = {
    'w': 'a',
    'k': 'b',
    'v': 'c',
    '1': 'd',
    'j': 'e',
    'u': 'f',
    '2': 'g',
    'i': 'h',
    't': 'i',
    '3': 'j',
    'h': 'k',
    's': 'l',
    '4': 'm',
    'g': 'n',
    '5': 'o',
    'r': 'p',
    'q': 'q',
    '6': 'r',
    'f': 's',
    'p': 't',
    '7': 'u',
    'e': 'v',
    'o': 'w',
    '8': '1',
    'd': '2',
    'n': '3',
    '9': '4',
    'c': '5',
    'm': '6',
    '0': '7',
    'b': '8',
    'l': '9',
    'a': '0'
}

# str 的translate方法需要用单个字符的十进制unicode编码作为key
# value 中的数字会被当成十进制unicode编码转换成字符
# 也可以直接用字符串作为value
char_table = {ord(key): ord(value) for key, value in char_table.items()}

# 解码图片URL
def decode(url):
    # 先替换字符串
    for key, value in str_table.items():
        url = url.replace(key, value)
    # 再替换剩下的字符
    return url.translate(char_table)

# 生成网址列表
def buildUrls(word):
    word = urllib.parse.quote(word)
    url = r"http://image.baidu.com/search/acjson?tn=resultjson_com&ipn=rj&ct=201326592&fp=result&queryWord={word}&cl=2&lm=-1&ie=utf-8&oe=utf-8&st=-1&ic=0&word={word}&face=0&istype=2nc=1&pn={pn}&rn=100"
    urls = (url.format(word=word, pn=x) for x in itertools.count(start=0, step=6))
    return urls

# 解析JSON获取图片URL
re_url = re.compile(r'"objURL":"(.*?)"')
def resolveImgUrl(html):
    imgUrls = [decode(x) for x in re_url.findall(html)]
    return imgUrls

def downImg(imgUrl, dirpath, imgName):
    filename = os.path.join(dirpath, imgName)
    try:
        res = requests.get(imgUrl, timeout=2)
        if str(res.status_code)[0] == "4":
            print(str(res.status_code), ":" , imgUrl)
            return False
    except Exception as e:
        print(" 异常条目内容：", imgUrl)
        print(e)
        return False
    with open(filename, "wb") as f:
        f.write(res.content)
    return True


def mkDir(dirName):
    #dirpath = os.path.join(sys.path[0].replace('\\', '\\'), dirName)
    if not os.path.exists(dirName):
        os.mkdir(dirName)
    return dirName

def downloadPic(words):
    
    word = words[0]
    picNum = int(words[1])
    dirpath = mkDir("下载\\" + str(word))
    print(dirpath)
    urls = buildUrls(word)
    index = 0
    for url in urls:
        print("请求url：", url)
        html = requests.get(url, timeout=2).content.decode('utf-8')
        imgUrls = resolveImgUrl(html)
        if len(imgUrls) == 0:  # 没有图片则结束
            print('已经没有图片了')
            break
        for url in imgUrls:
            if downImg(url, dirpath, str(word) + str(index) + ".jpg"):
                index += 1
                print("下载完第 %s 张图片" % index)
                if index == picNum:
                    sys.exit(0)
                




if __name__ == '__main__':

    print("=" * 50)
    start = time.clock()
    print('开始下载中。。。')
    wordFile = open('要下载的图片词条.txt', 'r', encoding = 'utf-8')
    wordList1 = [x.replace('\n', '') for x in wordFile.readlines()]
    print('请输入每个词条下载图片数目：')
    picNum = input()
    wordList = []
    for i in wordList1:
        wordList.append((i, picNum))

    #分布式下载
    agents = 4
    chunksize = int(len(wordList) / agents)
    pool = Pool(processes = agents)
    result = pool.map(downloadPic, wordList, chunksize)
    pool.close()
    pool.join()
    end = time.clock()
    print('所用时间为 %f 秒' %(end - start))
    print('爬取结束')
    sys.exit()