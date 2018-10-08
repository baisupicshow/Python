# from pypinyin import pinyin, lazy_pinyin, Style
#
# print(pinyin('中心'))
#
# #多音模式
# mul = pinyin('中心', heteronym=True)  # 启用多音字模式
# print(mul)



# import jieba
#
# seg_list = jieba.cut("我来到北京清华大学", cut_all=True)
# print("Full Mode: " + "/ ".join(seg_list))  # 全模式
#
# seg_list = jieba.cut("我来到北京清华大学", cut_all=False)
# print("Default Mode: " + "/ ".join(seg_list))  # 精确模式
#
# seg_list = jieba.cut("他来到了网易杭研大厦")  # 默认是精确模式
# print(", ".join(seg_list))
#
# seg_list = jieba.cut_for_search("小明硕士毕业于中国科学院计算所，后在日本京都大学深造")  # 搜索引擎模式
# print(", ".join(seg_list))

# import win32com.client
# speaker = win32com.client.Dispatch("SAPI.SpVoice")
# f = open('test.txt','r')
# speaker.Speak(f.read())

from aip import AipSpeech
""" 你的百度 APPID AK SK
https://console.bce.baidu.com/ai/#/ai/speech/app/list       应用列表
http://ai.baidu.com/docs#/TTS-Online-Python-SDK/top         API
"""
APP_ID = '10989511'
API_KEY = 'LKjcileZ5ib4bxSGHwcNQNt1'
SECRET_KEY = 'Q4pbFUMbHuS3IMhFl0qXQisgQuGbqgh9'

client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)
f = open('test.txt','rb')
text111 = f.read()
# result = client.synthesis(text111, lang='zh',ctp=1,{'vol': 5,})
result  = client.synthesis(text111, 'zh', 1, {
    'vol': 2,
})
# def synthesis(self, text, lang='zh', ctp=1, options=None):

# 识别正确返回语音二进制 错误则返回dict 参照下面错误码
if not isinstance(result, dict):
    with open('auido.wave', 'wb') as f:
        f.write(result)

with open('auido.pcm','rb') as mp:
    mp = mp.read()
text = client.asr(mp, 'pcm',16000, {
    'dev_pid': '1536',
})
print(text)