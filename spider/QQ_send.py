
from selenium import webdriver
path = "D:\Program Files\ChromeDriver\chromedriver.exe"
driver = webdriver.Chrome(executable_path=path)


login_url = 'https://www.douyu.com/688'
driver.get(login_url)
input("Press enter to continue")
# firend_list = []
# for eve_friend in driver.find_element_by_class_name("list_item"):
#     friend_list.append(eve_friend.find_element_by_xpath('a/@_uin').text)
