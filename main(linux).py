import ddddocr

from selenium import webdriver
import time
import  os

from selenium.webdriver.support.wait import WebDriverWait

ch_options = webdriver.ChromeOptions()
#为Chrome配置无头模式
ch_options.add_argument("--headless")
ch_options.add_argument('--no-sandbox')
ch_options.add_argument('--disable-gpu')
ch_options.add_argument('--disable-dev-shm-usage')

def mainWork ():
    path1 = os.getcwd()
    path1 = path1 + '/'

    user_name = []
    paw = []
    user_info_txt = open(path1 + 'user_info.txt', 'r')
    line = str(user_info_txt.readline())
    line = line.strip('\n')
    while line:
        user_name.append(line)
        line = str(user_info_txt.readline())
        line = line.strip('\n')
        paw.append(line)
        line = str(user_info_txt.readline())
        line = line.strip('\n')

    user_info_txt.close()


    for i in range(0, len(user_name)):
        def openWeb(driver1):
            driver1.get('http://sso.sdwz.cn/cas/login?service=http%3A%2F%2Fmy.sdwz.cn%2Flogin')

        while (True):
            driver = webdriver.Chrome(options=ch_options)
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
                captcha_img = driver.find_element_by_id('captchaAccount')
                return True

            WebDriverWait(driver, 10).until(login, message="")
            captcha_img = driver.find_element_by_id('captchaAccount')
            img = captcha_img.screenshot_as_png
            imgfile = open(path1 + 'CaptchaImg.png', 'wb')
            imgfile.write(img)
            imgfile.close()
            time.sleep(1.5)
            user = driver.find_element_by_id('username')
            password = driver.find_element_by_id('password')
            captcha_input = driver.find_element_by_id('captcha')
            login_button = driver.find_element_by_id('login-phone')

            # 验证码识别
            ocr = ddddocr.DdddOcr()
            with open("CaptchaImg.png", 'rb') as f:
                image = f.read()
            res = ocr.classification(image)
            print(res)

            user.send_keys(user_name[i])
            password.send_keys(paw[i])
            captcha_input.send_keys(res)
            time.sleep(10)
            driver.execute_script("arguments[0].click();", login_button)
            #login_button.click()
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
                #健康码颜色 绿色
                green = driver.find_element_by_xpath(
                    '/html/body/div[2]/div/div[1]/div/form/div/div[5]/div[2]/div[2]/div/div/span/label[1]/nobr/input')
                time.sleep(5)
                green.click()
                #当日是否进行核酸 否
                hesuan = driver.find_element_by_xpath(
                    '/html/body/div[2]/div/div[1]/div/form/div/div[6]/div[1]/div[2]/div/div/span/label[1]/nobr/input')
                time.sleep(5)
                hesuan.click()
                #共同居住者情况排查 无近期排查异常情况
                paicha = driver.find_element_by_xpath(
                    '/html/body/div[2]/div/div[1]/div/form/div/div[6]/div[2]/div[2]/div/div/span/label[1]/nobr/input')
                time.sleep(5)
                paicha.click()

                return True

            WebDriverWait(driver, 10).until(findGreen, message="")
            time.sleep(5)

            queding = driver.find_element_by_id('ext-gen25')
            queding.click()

        driver.close()
        driver.quit()
        if wrong_times <= 45:
            print(user_name[i] + ' 健康上报成功' + '\n')
        else:
            print(user_name[i] + ' 健康上报失败' + '\n')

if __name__ == "__main__":
    mainWork()
