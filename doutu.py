import requests
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
