# Get Data As Per User
from time import sleep
from main import db,DriverOptions,WebDriver,username,password,time,randint,BeautifulSoup
from tqdm import tqdm

def fetch_data(html,url):
    data = BeautifulSoup(html,"html.parser")
    data = data.find_all('section')
    dict_ = {}
    userName = data[0].find("h1").text if data[0].find("h1") else None
    dict_['username'] = userName
    dict_['url'] = url


    for i in range(1,len(data)):
        data_list = []
        
        i = data[i]
        topic = i.find("h2",class_="pvs-header__title").find("span") if i.find("h2",class_="pvs-header__title") else None

        if topic:
            topic = i.find("h2",class_="pvs-header__title").find("span").text if topic else None
            
            if not topic or "Education" in topic or "Experience" in topic:            
                pvs_list = i.find("div",class_="pvs-list__outer-container").find("ul",class_="pvs-list") if i.find("div",class_="pvs-list__outer-container") else None
                if pvs_list:
                    pvs_list = pvs_list.find_all("li")
                    
                   

                    for pvs in pvs_list:
                        dict_data = {}
                        each_segment = pvs.find("div",class_="display-flex flex-column full-width align-self-center")

                        if topic == "Experience" and each_segment:
                            detail_ = each_segment.find_all("span")
                            
                            try:
                                dict_data["profession"] = detail_[1].text if detail_[1] else None
                                dict_data["profession_description"] = detail_[4].text if detail_[4] else None
                            
                                dict_data["date_description"] = detail_[7].text if detail_[7] else None
                                dict_data["location"] = detail_[10].text if detail_[10] else None
                                dict_data["description"] = detail_[12].text if detail_[10] else None
                            except:
                                pass
                            
                            data_list.append(dict_data)
                        
                        if topic == "Education" and each_segment:
                            detail_ = each_segment.find_all("span")
                            
                           
                            try:
                                dict_data["college"] = detail_[1].text if detail_[1] else None
                                dict_data["student_course"] = detail_[4].text if detail_[4] else None
                                dict_data["year"] = detail_[7].text if detail_[7] else None
                            except:
                                pass
                            
                            data_list.append(dict_data)
        
                    dict_[topic] = data_list

    db.userData.insert_one(dict_)
            
def re_fetch_data(html,url):
    data = BeautifulSoup(html,"html.parser")
    data = data.find("section",class_="profile")
    userName = data.find("h1",class_="top-card-layout__title").text.strip() if data.find("h1",class_="top-card-layout__title") else None
    experience = data.find("section",class_="experience")
    education = data.find("section",class_="education") 

    experience = experience.find_all("div",class_="profile-section-card__contents")
    education = education.find_all("div",class_="profile-section-card__contents")

    dict_ = {"url":url,"username":userName}
    if experience:
        experience_list =[]
        for i in experience:
            dict_data = {}
            try:
                dict_data['profession'] = i.find("h3").text.strip() if i.find("h3") else None
                dict_data['profession_description'] = i.find("h4").text.strip() if i.find("h4") else None
                dict_data['date_description'] = i.find("p",class_="experience-item__duration").text.strip() if i.find("p",class_="experience-item__duration") else None
                dict_data['location'] = i.find("p",class_="experience-item__location").text.strip() if i.find("p",class_="experience-item__location") else None
            except:
                pass

            experience_list.append(dict_data)


    if education:
        education_list =[]
        for i in education:
            dict_data = {}
            try:
                dict_data['college'] = i.find("h3").text.strip() if i.find("h3") else None
                dict_data['student_course'] = i.find("h4").text.strip() if i.find("h4") else None
                dict_data['year'] = i.find("p",class_="education__item--duration").text.strip() if i.find("p",class_="education__item--duration") else None
                dict_data['description'] = i.find("p",class_="education__item--details").text.strip() if i.find("p",class_="education__item--details") else None
            except:
                pass

            education_list.append(dict_data)


    dict_["Experience"] = experience_list
    dict_["Education"] =  education_list


    db.userData.insert_one(dict_)

    
def start_fetch(driverinstance,url):
    try:
        # driverinstance.get(url)
        # url = (url.split("?")[0])
        # driverinstance.delete_all_cookies()
        # url = f"https://duckduckgo.com/?q=https%3A%2F%2Fwww.linkedin.com%2Fin%2F{url}&t=h_&ia=web"
        
        driverinstance.get(url)

        # time.sleep(randint(2,6))

        # try:
        #     user_data = driverinstance.find_element_by_id('main').get_attribute('innerHTML')                
        #     fetch_data(user_data,url)
        # except:   
        user_data = driverinstance.find_element_by_id('main-content').get_attribute('innerHTML')                
        re_fetch_data(user_data,url)
        
        # fetch_data(user_data)
        # dict_ = {"url":url}
        # try:
        #     name = driverinstance.find_element_by_xpath('//*[@id="ember557"]/div[2]/div[2]/div[1]/div[1]/h1').text
        # except:
        #     name = None
        # dict_['name'] = name 
        # dict_['html_data'] = user_data
        # db.userDataHtml.insert_one(dict_)
        # time.sleep(randint(5,10))
        print("\n\n")
        print(url)
        print("\n\n")
        
    except:
        # start_fetch(driverinstance,url)
        try:    
            current_url = driverinstance.current_url

            if "verification" in current_url or "challenge" in current_url:
                verify = input("yes or no: ")
                start_fetch(driverinstance,url)
            pass
        except:
            pass


def main(username,password):
    driver= WebDriver()
    driverinstance = driver.driver_instance

    # Login
    driverinstance.get('https://www.linkedin.com/login')
    time.sleep(randint(2,6))

    driverinstance.find_element_by_id("username").send_keys(username)
    driverinstance.find_element_by_id("password").send_keys(password)
    driverinstance.find_element_by_xpath('//*[@id="organic-div"]/form/div[3]/button').click()
    driverinstance.get('https://www.google.com/')
    


    time.sleep(randint(2,6))
    
    url_check = list(db.userData.distinct("url"))
    urls = db.dashboardUsers.distinct("url")

    urls = set(urls) - set(url_check) 
    
    for url in tqdm(urls):
        
        # if url not in url_check:
        start_fetch(driverinstance,url)






    print("---------------------------- Done ----------------------------------")

if __name__ == "__main__":
    main(username,password)