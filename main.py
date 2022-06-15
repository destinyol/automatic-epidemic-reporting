import requests

url='http://sso.sdwz.cn/cas/login?'
code_url = 'http://sso.sdwz.cn/cas/captcha'
headers={
    "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    "Accept-Language":"zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
    "Connection":"keep-alive",
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:101.0) Gecko/20100101 Firefox/101.0"
}
response = requests.get(url=url, headers=headers)
session = requests.session()

response_code = session.get(code_url)
content_code = response_code.content
with open('code.jpg', 'wb')as fp:
    fp.write(content_code)

code=input()
data = {
    "execution":"e2s1",
    "_eventId":"submit",
    "geolocation":"",
    "type":"1",
    "username":"2017404032",
    "password":"Pyf9081045",
    "captcha":code,
    "phone":"",
    "smsCode":"",
    "_rememberMe":"on"
}

response_post = session.post(url=url, headers=headers, data=data)
content_post = response_post.text
with open('gushiwen.html', 'w', encoding=' utf-8')as fp:
    fp.write(content_post)





