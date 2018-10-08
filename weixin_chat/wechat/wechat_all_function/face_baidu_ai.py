from aip import AipFace
import base64
""" 你的 APPID AK SK """
APP_ID = '11318363'
API_KEY = 'XGUtCiRDnkBifpzkCb2HvsVX'
SECRET_KEY = 'xNPE20MKkdHk3Ldu1OmzzIZhVK1T90uq'

client = AipFace(APP_ID, API_KEY, SECRET_KEY)


# image = "F:\pythonwork\weixin_chat\wechat\wechat_all_function\180529-141958.png"
with open('F:\\pythonwork\\weixin_chat\\wechat\\wechat_all_function\\180529-141958.png','rb') as f:
    image = base64.b64decode(f.read())
    print(image)
    imageType = "BASE64"



    """ 如果有可选参数 """
    options = {}
    options["face_field"] = "age"
    options["max_face_num"] = 2
    options["face_type"] = "LIVE"

    """ 带参数调用人脸检测 """
    message = client.detect(image, imageType, options)
    print(message)
    f.close()