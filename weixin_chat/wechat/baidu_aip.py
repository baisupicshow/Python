# coding:utf-8
import urllib.request, base64



access_token = '39fb27209e1f4fcba43d4b1e48488b4c'
url = 'https://aip.baidubce.com/rest/2.0/ocr/v1/general?access_token=' + access_token
# 二进制方式打开图文件
f = open(r'F:\百度aip\1.jpg', 'rb')
# 参数image：图像base64编码
img = base64.b64encode(f.read())
params = {"image": img}
params = urllib.request.urlencode(params)
request = urllib.Request(url, params)
request.add_header('Content-Type', 'application/x-www-form-urlencoded')
response = urllib.request.urlopen(request)
content = response.read()
if (content):
    print(content)