

from selenium import webdriver
from applitools.eyes import Eyes
from selenium.webdriver.common.action_chains import ActionChains
import time


def hover_over_my_tpt(driver):
    tpt_dropdown = driver.find_element_by_xpath("//div[@class='drop_down my_tpt']/a/span")
    hov = ActionChains(driver).move_to_element(tpt_dropdown).perform()



def test_logged_in_buyer():
    eyes = Eyes()
    eyes.api_key = 'u51qaFo104ruwwox0ewoWiFZQpijro9Z47fYTk1iQTozU110'

    driver = webdriver.Firefox()
    driver.maximize_window()

    try:
        eyes.open(driver=driver, app_name='Applitools', test_name='TpT Logged In Pages')

        # Login as buyer
        driver.get('http://www.teacherspayteachers.com/Login')
        driver.find_element_by_xpath("//input[@id='UserUsername']").clear()
        driver.find_element_by_xpath("//input[@id='UserUsername']").send_keys("buyer")
        driver.find_element_by_xpath("//input[@id='UserPassword']").clear()
        driver.find_element_by_xpath("//input[@id='UserPassword']").send_keys("123456")
        driver.find_element_by_xpath("//a[@class='common_button red fs_14 w_268 p_7 left_side login_button']").click()

        # Check Buyer's Dashboard
        eyes.check_window('Buyer Dashboard')
        time.sleep(10)
        driver.find_element_by_xpath("//div[@id='header2']/div[2]/div/div[4]/a[2]").click()

        # Login as seller
        driver.find_element_by_xpath("//input[@id='UserUsername']").clear()
        driver.find_element_by_xpath("//input[@id='UserUsername']").send_keys("testjayson")
        driver.find_element_by_xpath("//input[@id='UserPassword']").clear()
        driver.find_element_by_xpath("//input[@id='UserPassword']").send_keys("testing1")
        driver.find_element_by_xpath("//a[@class='common_button red fs_14 w_268 p_7 left_side login_button']").click()

        # Check Seller's Dashboard
        eyes.check_window('Seller\'s Dashboard')

        # Check My Account page
        driver.find_element_by_xpath("//div[@class='btns black']/a[1]").click()
        eyes.check_window('My Account page')

        # Check Store Profile page
        driver.find_element_by_xpath("//div[@class='left_side']/ul/li[2]").click()
        eyes.check_window('Store Profile page')

        # Check Payment Options page
        driver.find_element_by_xpath("//div[@class='left_side']/ul/li[3]").click()
        eyes.check_window('Payment Options Page')

        # Check Favorite Sellers page
        time.sleep(10)
        driver.find_element_by_xpath("//div[@class='left_side']/ul/li[4]").click()
        eyes.check_window('Favorite Sellers Page')

        # Check Referral Program page
        driver.find_element_by_xpath("//div[@class='left_side']/ul/li[5]").click()
        eyes.check_window('Referral Program Page')

        # Check Email Preference page
        time.sleep(10)
        driver.find_element_by_xpath("//div[@class='left_side']/ul/li[6]").click()
        eyes.check_window('Email Preference Page')

        # Purchase History Page
        time.sleep(10)
        driver.find_element_by_xpath("//div[@class='left_side']/ul/li[7]").click()
        eyes.check_window('Purchase History Page')

        # Sales & Earnings Page
        time.sleep(10)
        driver.find_element_by_xpath("//div[@class='left_side']/ul/li[8]").click()
        eyes.check_window('Sales & Earnings Page')


        hover_over_my_tpt(driver)
        driver.find_element_by_xpath("//div[@class='relative_container']/ul[3]/li[1]/a").click()

        # Check Promotions Page
        driver.find_element_by_xpath("//div[@class='two-columns-wrapper']/div[2]/div[2]/div[2]/a").click()
        eyes.check_window('Promotions Page')

        # Check Banners Page
        time.sleep(10)
        hover_over_my_tpt(driver)
        driver.find_element_by_xpath("//div[@class='relative_container']/ul[3]/li[1]/a").click()
        time.sleep(10)
        driver.find_element_by_xpath("//div[@class='two-columns-wrapper']/div[2]/div[4]/div[2]/a").click()
        eyes.check_window("Banners Page")

        # Check Product Upload Page
        hover_over_my_tpt(driver)
        driver.find_element_by_xpath("//div[@class='relative_container']/ul[3]/li[1]/a").click()
        driver.find_element_by_xpath("//div[@class='add']/a").click()
        eyes.check_window("Product Upload Page")

        # Check Product Listing Page
        hover_over_my_tpt(driver)
        driver.find_element_by_xpath("//div[@class='relative_container']/ul[3]/li[3]/a").click()
        eyes.check_window("Product Listing Page")

        # Check Product Statistics Page
        hover_over_my_tpt(driver)
        driver.find_element_by_xpath("//div[@class='relative_container']/ul[3]/li[4]/a").click()
        eyes.check_window("Product Statistics Page")

        # Check My Purchases page
        time.sleep(10)
        hover_over_my_tpt(driver)
        time.sleep(10)
        driver.find_element_by_xpath("//div[@class='relative_container']/ul[2]/li[2]/a").click()
        eyes.check_window("Check My Purchases page")

        eyes.close()

    finally:
        driver.quit()
        eyes.abort_if_not_closed()