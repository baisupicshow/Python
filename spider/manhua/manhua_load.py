import requests
url = 'http://www.hhmmoo.com/page307368/5.html?s=1&d=0'

req = requests.get(url)
print(req.json())
