__author__ = 'Roysten'

from selenium import webdriver
from applitools.eyes import Eyes
from selenium.webdriver.common.action_chains import ActionChains
import time


def hover_over_hamburger(driver):
    hamburger = driver.find_element_by_xpath("//div[@class='menu-bars-outer']/a/i")
    ActionChains(driver).move_to_element(hamburger).perform()

eyes = Eyes()
eyes.api_key = 'u51qaFo104ruwwox0ewoWiFZQpijro9Z47fYTk1iQTozU110'
driver = webdriver.Firefox()
driver.maximize_window()

try:
    eyes.open(driver=driver, app_name='itailor', test_name='itailors')
    driver.get('http://tailor.managedcoder.com/')
    hover_over_hamburger(driver)
    driver.find_element_by_xpath("//div[@class='menu-bars-item menu-bars-account']/ul/li[5]/a").click()
    driver.find_element_by_xpath("//input[@id='username']").send_keys("roystontestuser@gmail.com")
    driver.find_element_by_xpath("//input[@id='password']").send_keys("rash0207")
    driver.find_element_by_xpath("//input[@class='btn btn-default']").click()
    eyes.check_window("my account page")
    

except:
    driver.quit()
    eyes.abort_if_not_closed()