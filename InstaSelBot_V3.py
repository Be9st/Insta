from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep

NAME = 'artiommiastsov'
PASSWORD = '1q2w3e4r5tBe9st'

mobile_emulation = {
    "deviceMetrics": { "width": 360, "height": 640, "pixelRatio": 3.0 },
    "userAgent": "Mozilla/5.0 (Linux; Android 4.2.1; en-us; Nexus 5 Build/JOP40D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166 Mobile Safari/535.19" }
chrome_options = Options()
chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
driver = webdriver.Chrome(chrome_options = chrome_options)


driver.get("https://www.instagram.com/accounts/login/?source=auth_switcher/")
sleep(3)
login_form = driver.find_element_by_name('username')
login_form.send_keys(NAME)
password_form = driver.find_element_by_name('password')
password_form.send_keys(PASSWORD)


try: get_in = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div/div/div/form/div[6]/button')
except: get_in = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[7]/button')
get_in.click()
sleep(5)

#//*[@id="react-root"]/section/main/div/div[1]/div/div[1]/div[2]/div/a
#//*[@id="react-root"]/section/main/div/div[1]/div/div[2]/div[2]/div/a

otyebis = driver.find_element_by_xpath('/html/body/div[3]/div/div/div[3]/button[2]')
otyebis.click()

sleep(1)

driver.get('https://www.instagram.com/accounts/activity/')

sleep(50)
driver.close()