import pickle
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

# 0. Declare the browser
browser = webdriver.Chrome(executable_path="./chromedriver")

# 1. Open faceboook
browser.get("http://125.138.183.126/login_page.php")

# 2. Try to login

txtUser = browser.find_element_by_id("username")
txtUser.send_keys("huuhm")
txtUser.send_keys(Keys.ENTER)

txtPassword = browser.find_element_by_id("password")
txtPassword.send_keys("123456")

txtPassword.send_keys(Keys.ENTER)

sleep(10)

pickle.dump(browser.get_cookies(), open("my_cookie.pkl","wb"))

browser.close()