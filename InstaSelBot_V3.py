from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

driver = webdriver.Chrome()
driver.get("https://www.instagram.com/accounts/login/?source=auth_switcher/")
sleep(3)
login_form = driver.find_element_by_name('username')
login_form.send_keys('artiommiastsov')
password_form = driver.find_element_by_name('password')
password_form.send_keys('1q2w3e4r5tBe9st')
try: get_in = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[4]/button')
except: get_in = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[5]/button')
get_in.click()
sleep(3)
otyebis = driver.find_element_by_xpath('/html/body/div[3]/div/div/div[3]/button[2]')
otyebis.click()
sleep(25)
driver.close()