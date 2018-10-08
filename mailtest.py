# import smtplib
# from email.mime.text import MIMEText
# email_host = 'smtp.qq.com'     #邮箱地址
# email_user = '1431077852@qq.com'  # 发送者账号
# email_pwd = 'ntmugmsthryaijca'  # 发送者的密码
# maillist ='603516088@qq.com'  #收件人邮箱，多个账号的话，用逗号隔开
# me = email_user
# msg = MIMEText('这是个python测试邮件，不用回复。')    # 邮件内容
# msg['Subject'] = 'python测试'    # 邮件主题
# msg['From'] = me    # 发送者账号
# msg['To'] = maillist    # 接收者账号列表
# smtp = smtplib.SMTP(email_host,port=587) # 连接邮箱，传入邮箱地址，和端口号，smtp的端口号是25
# smtp.login(email_user, email_pwd)   # 发送者的邮箱账号，密码
# smtp.sendmail(me, maillist, msg.as_string())
# # 参数分别是发送者，接收者，第三个是把上面的发送邮件的内容变成字符串
# smtp.quit() # 发送完毕后退出smtp
# print ('email send success.')
#
# # !/usr/bin/python
# # -*- coding: UTF-8 -*-

import smtplib
from email.mime.text import MIMEText
from email.header import Header

# 第三方 SMTP 服务
mail_host = "smtp.qq.com"  # 设置服务器
mail_user = "1431077852@qq.com"  # 用户名
mail_pass = "ntmugmsthryaijca"  # 口令

sender = '1431077852@qq.com'
receivers = ['603516088@qq.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱

message = MIMEText('Python 邮件发送测试...', 'plain', 'utf-8')
message['From'] = Header("菜鸟教程", 'utf-8')
message['To'] = Header("测试", 'utf-8')

subject = 'Python SMTP 邮件测试'
message['Subject'] = Header(subject, 'utf-8')

try:
    smtpObj = smtplib.SMTP()
    smtpObj.connect(mail_host, 25)  # 25 为 SMTP 端口号
    smtpObj.login(mail_user, mail_pass)
    smtpObj.sendmail(sender, receivers, message.as_string())
    print("邮件发送成功")

except smtplib.SMTPException:
    print("Error: 无法发送邮件")