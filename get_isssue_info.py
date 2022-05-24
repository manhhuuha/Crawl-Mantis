from selenium.webdriver.common.keys import Keys
from time import sleep
import time
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
import csv
from selenium import webdriver
from selenium.webdriver.support.select import Select

def get_issue_info(project_url,project_name):
    save=[]
    # 0. Define browser
    browser = webdriver.Chrome(executable_path="./chromedriver")

    # 1. open Mantis                                              
    browser.get(project_url)

    # 2.Login
    txtUser = browser.find_element_by_id("username")
    txtUser.send_keys("huuhm")
    txtUser.send_keys(Keys.ENTER)

    txtPassword = browser.find_element_by_id("password")
    txtPassword.send_keys("123456")

    txtPassword.send_keys(Keys.ENTER)

    sleep(2)

    # 3. Refresh the browser
    bugPage=project_url+"view_all_bug_page.php"
    browser.get(bugPage)
    try:
        browser.find_element(By.XPATH,'//a[@id="custom_field_5_filter"]').click()
        # browser.find_element(By.XPATH,'//a[@id="hide_status_filter"]').click()
        browser.find_element(By.XPATH,'//a[@id="show_status_filter"]').click()
        browser.find_element(By.XPATH,'//a[@id="custom_field_1_filter"]').click()
        browser.find_element(By.XPATH,'//a[@id="per_page_filter"]').click()
        time.sleep(1)
        Select(browser.find_element(By.XPATH,'//select[@name="custom_field_5[]"]')).select_by_value(project_name)
        # Select(browser.find_element(By.XPATH,'//select[@name="hide_status[]"]')).select_by_value("-2")
        Select(browser.find_element(By.XPATH,'//select[@name="status[]"]')).select_by_value("80")
        Select(browser.find_element(By.XPATH,'//select[@name="custom_field_1[]"]')).select_by_value("Crawl_Failed")
        
        browser.find_element(By.XPATH,'//input[@name="per_page"]').send_keys("000")
    except Exception as e:
        print(e)
    # Select(browser.find_element_by_id(""))
    sleep(10)
    browser.find_element(By.XPATH,'//input[@value="Apply Filter"]').click()
    html = browser.page_source
    soup = BeautifulSoup(html,"html.parser")
    list_iss = soup.find_all("td",class_="column-id")
    for iss in list_iss:
        try:
            href= project_url+iss.find('a')['href']
            print(href)
            browser.get(href)
            soup = BeautifulSoup(browser.page_source,"html.parser")
            url = soup.find("td",class_="bug-description").find("a")["href"]
            bug_note = [x.get_text().replace("\n\t","").replace("\t","").replace("\n",'') for x in soup.find_all("td",class_="bugnote-note bugnote-public")]
            bug_date = soup.find("td",class_ = "bug-date-submitted").text
            save.append([url,bug_note,bug_date])
            time.sleep(0.5)
        except:
            print(iss)
    return save

def save_file(file_name,source):
    with open(file_name,'w',encoding='utf8',newline='') as f:
        writer = csv.writer(f)
        writer.writerows(source)