from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep

from db import connect_to_db

NAME = 'aleksmolik'
PASSWORD = '1q2w3e4r5t'
MESSAGE = 'Салам алейкум, брат!'

# настройки веб-дравйера
mobile_emulation = {
    "deviceMetrics": { "width": 360, "height": 640, "pixelRatio": 3.0 },
    "userAgent": "Mozilla/5.0 (Linux; Android 4.2.1; en-us; Nexus 5 Build/JOP40D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166 Mobile Safari/535.19" }
chrome_options = Options()
chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
driver = webdriver.Chrome(chrome_options = chrome_options)

# авторизация
driver.get("https://www.instagram.com/accounts/login/?source=auth_switcher/")
sleep(3)
login_form = driver.find_element_by_name('username')
login_form.send_keys(NAME)
password_form = driver.find_element_by_name('password')
password_form.send_keys(PASSWORD)

# кнопка авторизации + проверка на ублюдка
try: get_in = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div/div/div/form/div[6]/button')
except: get_in = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div/div/div/form/div[7]/button')
get_in.click()
sleep(3)

# послать нахуй уведомление
otyebis = driver.find_element_by_xpath('/html/body/div[3]/div/div/div[3]/button[2]')
otyebis.click()
sleep(1)

# открыть уведомления
driver.get('https://www.instagram.com/accounts/activity/')
sleep(1)


def main():
    ref = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div[1]/div/div[1]/div[2]/div/a')
    ref.click()
    sleep(1)
    user = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/div[1]/h1')

    if connect_to_db(user.text):
        print(4444)
        sleep(3)
        msg_btn = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/div[2]/div[1]/button')
        msg_btn.click()
        sleep(3)

        text_box = driver.find_element_by_xpath('//*[@id="react-root"]/section/div[2]/div[2]/div/div/div/textarea')
        text_box.send_keys(MESSAGE)
        sleep(1)
        print(3333)
        send_button = driver.find_element_by_xpath('//*[@id="react-root"]/section/div[2]/div[2]/div/div/div[2]/button')
        send_button.click()
    else:
        print(2222)
        sub = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/div[2]/div/span/span[1]/button')
        sub.click()
        sleep(3)

        msg_btn = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/div[2]/div[1]/button')
        msg_btn.click()
        sleep(3)

        text_box = driver.find_element_by_xpath('//*[@id="react-root"]/section/div[2]/div[2]/div/div/div/textarea')
        text_box.send_keys(MESSAGE)
        sleep(1)
        print(1111)
        send_button = driver.find_element_by_xpath('//*[@id="react-root"]/section/div[2]/div[2]/div/div/div[2]/button')
        send_button.click()


if __name__ == "__main__":
    while True:
        try: 
            main()
        except: 
            driver.get('https://www.instagram.com/accounts/activity/')
            print('sleeepiiiingggg')
            sleep(15)