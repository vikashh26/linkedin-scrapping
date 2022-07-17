from random import randint
from sqlite3 import connect
from attr import attr
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from main import db,DriverOptions,WebDriver,username,password
import time
import pymongo




user_check = db.dashboardUsers.distinct('url')

def fetch_data(html):
    data = BeautifulSoup(html,"html.parser")
    data = data.find_all('li')
    for i in data:
        dict_ = {}
        dict_['url'] = i.find("a",class_="app-aware-link")['href']
        dict_['description'] = i.find("p",class_="entity-result__summary").text if i.find("p",class_="entity-result__summary") is not None else None
        dict_['location'] = i.find("div",class_="entity-result__secondary-subtitle").text if i.find("div",class_="entity-result__secondary-subtitle") is not None else None
        if dict_['url'] not in user_check:
            db.dashboardUsers.insert_one(dict_)


def follow_people(driverinstance):
    pass


def main(username,password):
    a = 80
    driver= WebDriver()
    driverinstance = driver.driver_instance
    driverinstance.get("https://www.linkedin.com/uas/login?session_redirect=https%3A%2F%2Fwww%2Elinkedin%2Ecom%2Fsearch%2Fresults%2Fpeople%2F%3Fkeywords%3Drohit%2520iit%26origin%3DGLOBAL_SEARCH_HEADER%26sid%3DNyH&fromSignIn=true&trk=cold_join_sign_in")
    driverinstance.find_element_by_id("username").send_keys(username)
    driverinstance.find_element_by_id("password").send_keys(password)
    time.sleep(randint(2,6))
    driverinstance.find_element_by_xpath('//*[@id="organic-div"]/form/div[3]/button').click()
    time.sleep(randint(2,6))


    if "verification" in driverinstance.current_url or "challenge" in driverinstance.current_url:
            verify = input("yes or no: ")

    div_count = "1"
    try:
        user_html_list = driverinstance.find_element_by_xpath('//*[@id="main"]/div/div/div[1]/ul').get_attribute('innerHTML')
    except:
        user_html_list = driverinstance.find_element_by_xpath('//*[@id="main"]/div/div/div[2]/ul').get_attribute('innerHTML')
        div_count = "2"

    fetch_data(user_html_list)
    time.sleep(randint(5,15))

    for i in range(2,101):
        page = f"&page={i}"
        driverinstance.get(f"https://www.linkedin.com/search/results/people/?keywords=rohit%20iit&origin=GLOBAL_SEARCH_HEADER&{page}")
        # driverinstance.find_element_by_xpath('/html/body/div[6]/div[3]/div/div[2]/div/div[1]/main/div/div/div/div[2]/div/button[2]').click()
        if "verification" in driverinstance.current_url or "challenge" in driverinstance.current_url:
            verify = input("yes or no: ")
        time.sleep(randint(2,6))

        user_html_list = driverinstance.find_element_by_xpath(f'//*[@id="main"]/div/div/div[{div_count}]/ul').get_attribute('innerHTML')
        # if a >= 1:
        #     connect_button = []
        #     try:
        #         connect_button = driverinstance.find_elements_by_class_name("artdeco-button.artdeco-button--2.artdeco-button--secondary.ember-view")
        #     except:
        #         pass        
        #     for i in connect_button:
        #         if "Message" not in i.text:
        #             try: 
        #                 i.click()

        #                 driverinstance.find_element_by_xpath('//*[@id="ember1508"]').click()
        #                 time.sleep(1)
        #                 a -= 1
        #             except:
        #                 pass

        try:
            fetch_data(user_html_list)
        except:
            break

        print("-"*25,i,"-"*25)
        time.sleep(randint(5,10))



    driverinstance.close()
    print("---------------------------- Done ----------------------------------")

if __name__ == "__main__":
    main(username,password)