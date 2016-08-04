__author__ = 'Roysten'

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from urllib.request import urlretrieve
import urllib
import os
import time
import pytest
import csv
from selenium.common.exceptions import NoSuchElementException


#heading_field_locator = (By.XPATH, "//h1[@id='firstHeading']")
#paragraph_field_locator = (By.XPATH, "//div[@id='mw-content-text']/p")
#image_field_locator = (By.XPATH, "//div[@id='mw-content-text']/table/tbody/tr[2]/td/a/img")
#search_text_field_locator = (By.XPATH, "//input[@id='searchInput']")
#search_button_field_locator = (By.XPATH, "//input[@id='searchButton']")
#def test_scrapping():



driver = webdriver.Firefox()
with open('baseball_players.csv') as csv_file:
   readCSV = csv.reader(csv_file, delimiter=',')
   names = []
   for row in readCSV:
       n = row[0]
       names.append(n)

j = 1

for i in range(0, len(names)):
    driver.get("https://en.wikipedia.org/wiki/")
    driver.find_element_by_xpath("//input[@id='searchInput']").click()
    driver.find_element_by_xpath("//input[@id='searchInput']").send_keys(names[i])
    driver.find_element_by_xpath("//input[@id='searchButton']").click()
    heading = driver.find_element_by_xpath("//h1[@id='firstHeading']").text
    print(heading)
    paragraph = driver.find_element_by_xpath("//div[@id='mw-content-text']/p").text
    print(paragraph.encode('utf8'))
    try:
        image = driver.find_element_by_xpath("//div[@id='mw-content-text']/table/tbody/tr[2]/td/a/img")
        src = image.get_attribute('src')
        new_path ='C:\project\data scrap(baseball)\images'

        saved_image = urlretrieve(src, new_path+ '\\baseball_player.png')
        '''if not os.path.exists(new_path):
            os.makedirs(new_path)
        urllib.request.urlretrieve(saved_image, "PATH"+os.path.basename(saved_image))'''
    except NoSuchElementException:
        print("Locators are not found")


    if j == 1:
        driver.get("http://TBP:devtbp@123@thebaseballpage.managedcoder.com/")
        driver.find_element_by_xpath("//input[@id='edit-name']").send_keys("admin")
        driver.find_element_by_xpath("//input[@id='edit-pass']").send_keys("admin@123")
        driver.find_element_by_xpath("//input[@id='edit-submit--2']").click()
        j = j + 1
    else:
        driver.get("http://thebaseballpage.managedcoder.com/node/add/baseball-player")
        driver.find_element_by_xpath("//input[@id='edit-title']").send_keys(heading)
        driver.find_element_by_xpath("//textarea[@id ='edit-body-und-0-value']").send_keys(paragraph)
        #driver.find_element_by_xpath("//div[@class='image-widget-data']/input[1]").click()
        driver.find_element_by_xpath("//div[@class='image-widget-data']/input[1]").send_keys("C:\\project\\data scrap(baseball)\\images\\baseball_player.png")
        time.sleep(30)
        driver.find_element_by_xpath("//input[@id='edit-submit']").click()
        i = i + 1
        print(i)




