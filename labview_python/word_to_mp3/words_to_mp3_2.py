from aip import AipSpeech
import sys

APP_ID = 'xxxxxxxxxxx'  # 从百度AI注册获取，免费
API_KEY = 'xxxxxxxxxxxxxxxxxxxxxx'
SECRET_KEY = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)
result = client.synthesis(sys.argv[1],'zh', 1, {'spd':sys.argv[2], 'vol': 5,'per': sys.argv[3]})

    # 识别正确返回语音二进制 错误则返回dict 参照下面错误码

# voice = gen_voice(sys.argv[1])
# if not isinstance(voice, dict):
#         with open(sys.argv[2], 'wb') as f:
#             f.write(voice)


# if not isinstance(voice, dict):
#     b = sys.argv[2]
#     print(sys.argv[2])
#     with open( b, 'wb') as f:
#         f.write(sys.argv[2])
f=open(sys.argv[4],'wb')
f.write(result)#写入的字符串包含多个换行符，可以达到写入多行的效果
f.close()
print('生成成功')