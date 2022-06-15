import os
import smtplib
# 发送字符串的邮件
from email.mime.text import MIMEText
# 需要 MIMEMultipart 类
from email.mime.multipart import MIMEMultipart


# 设置服务器所需信息

def send_mail(toEmails,path1):
    sendemail_info_txt = open(path1 + 'sendemail_config.txt', 'r')
    info1 = str(sendemail_info_txt.readline()).strip('\n')
    info2 = str(sendemail_info_txt.readline()).strip('\n')
    fromEmailAddr = info1  # 邮件发送方邮箱地址
    password = info2  # (注意不是邮箱密码，而是为授权码)
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
    ids = []
    # dic = {'2100404045': '失败', '2100404046': '成功', '2017404032': '失败'}
    dic = d
    # 遍历字典列表

    for key, values in dic.items():
        # print (key, values)
        if values == '失败':
            ids.append(key)
    print(ids)

    path1 = os.getcwd()
    path1 = path1 + '/'

    emails = []
    need_mail = False
    emails_info_txt = open(path1 + 'id_to_emails.txt', 'r')
    line = str(emails_info_txt.readline())
    line = line.strip('\n')
    while line:
        need_mail = False
        for i in ids:
            if line == i:
                need_mail = True
        line = str(emails_info_txt.readline())
        line = line.strip('\n')
        if need_mail:
            emails.append(line)
        line = str(emails_info_txt.readline())
        line = line.strip('\n')

    emails_info_txt.close()
    print(emails)
    send_mail(emails,path1)
