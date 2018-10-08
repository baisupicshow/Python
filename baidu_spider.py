import re
import requests
from bs4 import BeautifulSoup
from lxml import etree
# r = requests.get('http://ip.taobao.com/service/getIpInfo.php?ip=122.88.60.28')
# k = r.json()['data']['country']
# print(k)
# r = requests.get('http://image.baidu.com/search/index?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&fm=result&fr=&sf=1&fmq=&pv=&ic=0&nc=1&z=&se=&showtab=0&fb=0&width=&height=&face=0&istype=2&ie=utf-8&ctd=&word=%E9%87%91%E5%B1%B1')
# k = r.json()
# print(k)
# print(json.dumps([2]))

url = 'http://www.dytt8.net/'
# headers = {
#     'user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.3'
# }
r = requests.get(url)
# print(type(r.text))
# print(r.json())
print(r.json())

# headers = {
#     'user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.3'
# }
# data = {'name':'germey','age':'22'}
# response = requests.get(url,data = data,headers=headers)