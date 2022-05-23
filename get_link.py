
import json
import pickle
from selenium.webdriver.common.keys import Keys
from time import sleep
import time
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
import csv
from selenium import webdriver
from selenium.webdriver.support.select import Select

save=[]
# 0. Define browser
browser = webdriver.Chrome(executable_path="./chromedriver")

hyundai = "http://114.200.204.68:8080/"
deepSignal = "http://125.138.183.126/"
# 1. open Mantis                                              
browser.get(hyundai)

# 2.Login
txtUser = browser.find_element_by_id("username")
txtUser.send_keys("huuhm")
txtUser.send_keys(Keys.ENTER)

txtPassword = browser.find_element_by_id("password")
txtPassword.send_keys("123456")

txtPassword.send_keys(Keys.ENTER)

sleep(5)

# cookies = pickle.load(open("my_cookie.pkl","rb"))
# for cookie in cookies:
#     browser.add_cookie(cookie)

# 3. Refresh the browser
bugPage=hyundai+"view_all_bug_page.php"
browser.get(bugPage)
browser.find_element(By.XPATH,'//a[@id="custom_field_5_filter"]').click()
# browser.find_element(By.XPATH,'//a[@id="hide_status_filter"]').click()
browser.find_element(By.XPATH,'//a[@id="show_status_filter"]').click()
browser.find_element(By.XPATH,'//a[@id="custom_field_1_filter"]').click()
browser.find_element(By.XPATH,'//a[@id="per_page_filter"]').click()
time.sleep(1)
Select(browser.find_element(By.XPATH,'//select[@name="custom_field_5[]"]')).select_by_value("Hyundai In-Service")
# Select(browser.find_element(By.XPATH,'//select[@name="hide_status[]"]')).select_by_value("-2")
Select(browser.find_element(By.XPATH,'//select[@name="status[]"]')).select_by_value("80")
Select(browser.find_element(By.XPATH,'//select[@name="custom_field_1[]"]')).select_by_value("Crawl_Failed")
browser.find_element(By.XPATH,'//input[@name="per_page"]').send_keys("000")
# Select(browser.find_element_by_id(""))
browser.find_element(By.XPATH,'//input[@value="Apply Filter"]').click()
html = browser.page_source
soup = BeautifulSoup(html,"html.parser")
list_iss = soup.select("td.column-id")
for iss in list_iss:
    try:
        href= hyundai+iss.find('a')['href']
        browser.get(href)
        soup = BeautifulSoup(browser.page_source,"html.parser")
        url = soup.find("td",class_="bug-description").find("a")["href"]
        bug_note = [x.get_text().replace("\n\t","").replace("\t","") for x in soup.find_all("td",class_="bugnote-note bugnote-public")]
        save.append([url,bug_note])
        time.sleep(0.5)
    except:
        print(iss)

with open("data.csv","w",encoding="utf8",newline='') as f:
    write=csv.writer(f)
    write.writerows(save)
time.sleep(20)