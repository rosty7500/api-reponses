__author__ = 'Roysten'


import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from pages.base_url1 import base_url


#driver = webdriver.Firefox()

class login():

    def login(self,driver):
        base_url()
        #driver.maximize_window()
        #driver.get('http://hullforest.managedcoder.com/account/login')
        #cookies_list = driver.get_cookies()
        #cookies_dict = {}
        #for cookie in cookies_list:
        #   cookies_dict[cookie['name']] = cookie['value']
        #print(cookies_dict)
        element = driver.find_element_by_id("input-email")
        element.send_keys("roystontestuser@gmail.com")
        element1 = driver.find_element_by_id("input-password")
        element1.send_keys("12345678")
        element9 = driver.find_element_by_xpath("//input[@class='btn btn-primary button']").click()
        if driver.find_element_by_xpath("//div[@class='links j-min']/a[1]/span").text == "roy":
            assert True
        else:
            assert False
