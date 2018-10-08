from aip import AipSpeech
import sys

def gen_voice(words):
    APP_ID = 'xxxxxxxxxxxx'  # 从百度AI注册获取，免费
    API_KEY = 'xxxxxxxxxxxxxxxx'
    SECRET_KEY = 'xxxxxxxxxxxxxxxxxxxxxxxxxxx'
    client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)
    result = client.synthesis(words,'zh', 1, {'vol': 3,'per': 4})
    return result
    # 识别正确返回语音二进制 错误则返回dict 参照下面错误码

# voice = gen_voice(sys.argv[1])
# if not isinstance(voice, dict):
#         with open(sys.argv[2], 'wb') as f:
#             f.write(voice)

voice = gen_voice(sys.argv[1])
# if not isinstance(voice, dict):
#     b = sys.argv[2]
#     print(sys.argv[2])
#     with open( b, 'wb') as f:
#         f.write(sys.argv[2])
f=open(sys.argv[2],'wb')
f.write(voice)#写入的字符串包含多个换行符，可以达到写入多行的效果
f.close()
print('生成成功')