import os
import json
import smtplib
# 发送字符串的邮件
from email.mime.text import MIMEText
# 需要 MIMEMultipart 类
from email.mime.multipart import MIMEMultipart


# 设置服务器所需信息

def send_mail(toEmails):
    with open("sendemail_config.json", 'r', encoding='utf-8') as fw:
        injson = json.load(fw)
    fromEmailAddr = injson[EmailAddress]  # 邮件发送方邮箱地址
    password = injson[Authorization_code]  # (注意不是邮箱密码，而是为授权码)
    # 邮件接受方邮箱地址，注意需要[]包裹，这意味着你可以写多个邮件地址群发
    toEmailAddrs = toEmails
    # 设置email信息
    # ---------------------------发送带附件邮件-----------------------------
    # 邮件内容设置
    message = MIMEMultipart()
    # 邮件主题
    message['Subject'] = 'python test email'
    # 发送方信息
    message['From'] = fromEmailAddr
    # 接受方信息
    message['To'] = 'dear'
    # 邮件正文内容
    message.attach(MIMEText('你的自动健康上报已出错，请手动上报', 'plain', 'utf-8'))
    # 构造附件
    # ---------------------------------------------------------------------
    # 登录并发送邮件
    try:
        server = smtplib.SMTP('smtp.qq.com')  # qq邮箱服务器地址，端口默认为25
        server.login(fromEmailAddr, password)
        server.sendmail(fromEmailAddr, toEmailAddrs, message.as_string())
        print('success')
        server.quit()
    except smtplib.SMTPException as e:
        print("error:", e)


# send_mail()

def if_send(d):
    with open("option.json", 'r', encoding='utf-8') as fw:
        injson = json.load(fw)
    if injson[emailReminder] == "close":
        return
    ids = []
    dic = d
    # 遍历字典列表

    for key, values in dic.items():
        # print (key, values)
        if values == '失败':
            ids.append(key)
    print(ids)

    emails = []
    need_mail = False
    with open("id_to_emails.json", 'r', encoding='utf-8') as fw:
        dic_info = json.load(fw)
    for j in ids:
        need_mail = False
        if j in dic_info:
            need_mail = True
        if need_mail:
            emails.append(dic_info[j])

    # print(emails)
    send_mail(emails)
