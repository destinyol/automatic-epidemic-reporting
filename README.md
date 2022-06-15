# automatic-epidemic-reporting
苏州城市学院自动疫情上报

# 介绍
  程序功能是基于selenium实现的，运行性能不高，但也够用

  本来打算用python爬虫实现，奈何水平不足
  
  支持一个或多个学生的疫情上报，并可以做到失败后的逐个邮箱提醒
  
  使用本程序需要安装google chrome浏览器
  
  -----仅供学习与交流，自行承担相应后果-----

# selenium chromc驱动下载地址
  https://registry.npmmirror.com/binary.html?path=chromedriver/

  selenium的运行需要对应的驱动

  注意chrome的版本与驱动版本相对应

  驱动文件放到python根目录下(linux需要放置在/usr/bin/中,并添加执行权限，请查阅相关资料)

  windows10一般为: C:\Users\asus\AppData\Local\Programs\Python\Python39
  
  在此，感谢[ddddocr](https://github.com/sml2h3/ddddocr)的技术支持。相关依赖下载如下：
  ```
  pip install ddddocr
  //pip3 install ddddocr
  ```

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
  
### 5.邮件发送相关配置文件
  id_to_emails.json文件中键值对是接受邮件的学号和与之对应的邮箱
  
  sendemail_config.json文件中键值对是发送邮件信息的邮箱的账号和授权码
  
  发送邮件需要一个开启[IMAP/SMTP服务](https://service.mail.qq.com/cgi-bin/help?subtype=1&&id=28&&no=331)的邮箱账号，当你开启这个服务时，邮件运营商会给你提供一个授权码。
  将其填入sendamail_config.json中。
  
### 6.云服务器部署问题
  在服务器上git clone本项目，填写相关json文件配置。注意，需要添加python依赖库。(pip安装)，即可运行。
  
  ~~如果生成log文件失败，可在项目目录中手动添加空log目录。~~(目前git文件夹已提供log目录)
  
  若想自动定时运行该py脚本，则可利用Crontab工具，
  ```
  0 8 * * * python3 /../../automatic-epidemic-reporting/start.py
  ```
  每天8:00自动执行任务。注意要采用绝对路径!(请查阅相关资料)
