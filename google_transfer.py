import requests  
import re
word = 'beautiful'
url = 'https://translate.google.cn/?hl=zh-CN&tab=TT#auto/zh-CN/' + word
# print(url)

r = requests.post(url)
print(r.text)
s =re.findall(' <span class="">(.*?)</span>',r.text)
