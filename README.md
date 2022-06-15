# automatic-epidemic-reporting
苏州城市学院自动疫情上报

# 介绍
  程序功能是基于selenium实现的，运行性能不高，但也够用

  本来打算用python爬虫实现，奈何水平不足
  
  支持一个或多个学生的疫情上报，并可以做到失败后的逐个邮箱提醒
  
  使用本程序需要安装google chrome浏览器

# selenium chromc驱动下载地址
  https://registry.npmmirror.com/binary.html?path=chromedriver/

  selenium的运行需要对应的驱动

  注意chrome的版本与驱动版本相对应

  驱动文件放到python根目录下

  windows10一般为: C:\Users\asus\AppData\Local\Programs\Python\Python39

# 使用说明
### 1.启动文件是 start.py 

### 2.软件配置文件 option.json

  "browser"  为"true"：显示浏览器界面，为"false"：浏览器后台运行，不显示界面
  
  "localLog"  为"open"：打开本地日志功能，为"close"：关闭本地日志功能
  
  "emailReminder"  为"open"：打开每日健康上报邮件提醒功能，若有学号上报成功或失败则将发送邮件给对应的学号对应的邮箱，为"close"：关闭每日健康上报邮件提醒功能
  
  "emailSucessFail"  为"true"：上报成功或失败都邮箱提醒，为"false"：上报失败提醒，成功则不提醒
  
### 3.学号密码的输入 user_info.json
  支持一个或多位学生，程序将由线性结构依次进行疫情上报
  
  数据格式:
  
            "2017xxxxxx":"xxxxxxx",
            "1917xxxxxx":"xxxxxx"
  
### 4.windows本地开机启动后台运行自动化配置：
  将"启动.vbs"文件创建快捷方式，并将快捷方式放至
  
  C:\Users\用户名\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup
  
  (AppData是隐藏文件夹，找不到记得打开显示隐藏文件夹)
