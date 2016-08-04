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
    #clicks on login/register link
    driver.find_element_by_xpath("//div[@class='menu-bars-item menu-bars-account']/ul/li[5]/a").click()

    #enter login credentails
    driver.find_element_by_xpath("//input[@id='username']").send_keys("roystontestuser@gmail.com")
    driver.find_element_by_xpath("//input[@id='password']").send_keys("rash0207")
    driver.find_element_by_xpath("//input[@class='btn btn-default']").click()
    #check account page
    eyes.check_window("my account page")
    #check edit account page
    driver.find_element_by_xpath("//p[@class='myaccount_user']/a[2]").click()
    eyes.check_window("edit account")
    #go to product page
    driver.find_element_by_xpath("//div[@class='container']/nav/ul/li[2]/a").click()
    #add product to cart
    driver.find_element_by_xpath("//form[@class='cart']/button").click()
    driver.find_element_by_xpath("//div[@class='menu-bars-item menu-bars-account']/ul/li[3]/a").click()
    eyes.check_window("cart with products")
    #add to wishlist
    driver.find_element_by_xpath("//div[@class='yith-wcwl-add-to-wishlist add-to-wishlist-96']/div[1]/a").click()
    driver.find_element_by_xpath("//div[@class='yith-wcwl-add-to-wishlist add-to-wishlist-96']/div[1]/a").click()
    eyes.check_window("wishlist with products")

    #compare the products for logged in user when products are already added to compare
    hover_over_hamburger(driver)
    driver.find_element_by_xpath("//div[@class='menu-bars-item menu-bars-account']/ul/li[2]/a").click()
    eyes.check_window("compare when products are already added to compare")


except:
    driver.quit()
    eyes.abort_if_not_closed()