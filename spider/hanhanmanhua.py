'''
mport requests
import re
import image
# import pymysql

# db = pymysql.connect(host = '127.0.0.1', port = 3306, db = 'mypydb', user = 'root', passwd = '123456', charset = 'utf8')
# cursor = db.cursor()
# cursor.execute('select * from images')

for i in range(1,1000):
    url = 'http://www.doutula.com/photo/list/?page=' + str(i)
    # print(url)
    response = requests.get(url).text
    # # print(response.text)
    reg = r'data-original="(.*?)".*?alt="(.*?)"'
    reg = re.compile(reg, re.S)
    # pic_url = re.findall('data-original="(.*?)".*?alt="(.*?)"',response)
    urlList = re.findall(reg, response)
    # print(urlList)
    for getPicUrl in urlList:
        name = getPicUrl[1]
        picUrl = getPicUrl[0]
        img = requests.get(picUrl)
        # print(img.text)
        path = 'E:\\斗图啊\\' + name + '.jpg'
        # with open('path','ab') as f:
        #     f.write(img.content)
        #     f.close()
        print(path)
        r = requests.get(picUrl,stream=True)
        with open(path, 'wb') as fd:
            for chunk in r.iter_content():
              fd.write(chunk)

        # cursor.execute("insert into images('name','imageUrl') values('{}','{}')".format(getPicUrl[1],getPicUrl[0]))
        # print('正在保存')
        # db.commit()



import requests
import re

url = 'http://www.popomh.com/popo269459/5.html?s=8&d=0'
response = requests.get(url).text
# print(response)
reg = r'<img.src=(.*?)'
pic_url = re.findall(reg , response)
print(pic_url)
'''


'''

element.style {
}
body {
    font-size: 14px;
    margin: 0px;
    text-align: center;
    background-color: #FFFFFF;
}
'''

'''成功提取src

from lxml import html
import requests

from lxml import html
url = 'https://movie.douban.com/chart'

r = requests.get(url).content
sel = html.fromstring(r)

# 提取h1标签
title = sel.xpath("//a/img/@src")
# 提取链接
links = sel.xpath('//div[@class="pl2"]/a/@href')
print(title[0])
# 上面返回的是所有符合条件的链接的列表，for循环来读取一下
for link in links:
    print (link)
'''


import re
import requests

#url内输入你要下载的图片地址

url = 'http://www.popomh.com/popo306606/1.html?s=1'

html = requests.get(url).text
pic_url = re.findall('"objURL":"(.*?)",',html,re.S)

# 提取链接

print(pic_url)
