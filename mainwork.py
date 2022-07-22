import ddddocr
import time
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
import json
import os

def mainWork ():
    log = {}
    user_name = []
    paw = []
    path = os.path.dirname(os.path.realpath(__file__)) + '/'
    with open(path + "user_info.json", 'r', encoding='utf-8') as fw:
        data = json.load(fw)
    for i in data.items():
        user_name.append(i[0])
        paw.append(i[1])
        log[i[0]] = "失败"
    with open(path + "option.json", 'r', encoding='utf-8') as fw:
        injson = json.load(fw)

    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-gpu')
    options.add_argument('--disable-dev-shm-usage')

    for i in range(0, len(user_name)):
        try:
            def openWeb(driver1):
                driver1.get('http://sso.sdwz.cn/cas/login?service=http%3A%2F%2Fmy.sdwz.cn%2Flogin')

            while (True):
                if injson['browser'] == 'false':
                    driver = webdriver.Chrome(options=options)
                else:
                    driver = webdriver.Chrome()
                driver.implicitly_wait(10)

                try:
                    openWeb(driver)
                    time.sleep(3)
                    break

                except:
                    driver.quit()

            wrong_times = 0
            while 1:
                wrong_times = wrong_times + 1
                if wrong_times > 45:
                    print('错误重复次数大于45次，可能验证码识别模块出现问题，当前循环终止')
                    break
                print('登陆中....')

                def login(x):
                    driver.find_element_by_id('captchaAccount')
                    return True

                WebDriverWait(driver, 10).until(login, message="")
                captcha_img = driver.find_element_by_id('captchaAccount')
                img = captcha_img.screenshot_as_png
                imgfile = open(path + 'CaptchaImg.png', 'wb')
                imgfile.write(img)
                imgfile.close()
                time.sleep(1.5)
                user = driver.find_element_by_id('username')
                password = driver.find_element_by_id('password')
                captcha_input = driver.find_element_by_id('captcha')
                login_button = driver.find_element_by_id('login-phone')
                ocr = ddddocr.DdddOcr()
                with open(path + "CaptchaImg.png", 'rb') as f:
                    image = f.read()
                res = ocr.classification(image)

                user.send_keys(user_name[i])
                password.send_keys(paw[i])
                captcha_input.send_keys(res)
                time.sleep(1)
                driver.execute_script("arguments[0].click();", login_button)
                time.sleep(5)
                try:
                    driver.find_element_by_xpath('/html/body/div/div/div[2]/div/div/div[2]/div[2]/form/div[1]/span')
                    print('验证码错误')

                except:
                    print('登录成功')
                    break

            if wrong_times <= 45:
                jksb = driver.find_element_by_xpath(
                    '/html/body/div[3]/div/div/div[2]/div/div[3]/div/div/div/div[1]/div[3]/a')
                jksb.click()

                handles = driver.window_handles
                driver.switch_to.window(handles[1])

                def findGreen(x):
                    # 健康码颜色 绿色
                    green = driver.find_element_by_xpath(
                        '/html/body/div[2]/div/div[1]/div/form/div/div[5]/div[2]/div[2]/div/div/span/label[1]/nobr/input')
                    green.click()
                    # 当日是否进行核酸 否
                    hesuan = driver.find_element_by_xpath(
                        '/html/body/div[2]/div/div[1]/div/form/div/div[6]/div[1]/div[2]/div/div/span/label[1]/nobr/input')
                    hesuan.click()
                    # 共同居住者情况排查 无近期排查异常情况
                    paicha = driver.find_element_by_xpath(
                        '/html/body/div[2]/div/div[1]/div/form/div/div[6]/div[2]/div[2]/div/div/span/label[1]/nobr/input')
                    paicha.click()
                    return True

                WebDriverWait(driver, 10).until(findGreen, message="")
                time.sleep(5)

                queding = driver.find_element_by_id('ext-gen25')
                queding.click()
                time.sleep(1.5)

            if wrong_times <= 45:
                print(user_name[i] + ' 健康上报成功' + '\n')
                log[user_name[i]] = "成功"
            else:
                print(user_name[i] + ' 健康上报失败' + '\n')
        except:
            pass
        finally:
            driver.close()
            driver.quit()

    return log
