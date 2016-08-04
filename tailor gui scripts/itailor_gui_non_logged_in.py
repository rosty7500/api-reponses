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

    #homepage_new_arrivals
    driver.get('http://tailor.managedcoder.com/')
    eyes.check_window("homepage_new_arrivals")

    #homepage_hot_products
    driver.find_element_by_xpath("//div[@class='entry-content clearfix']/div[2]/div/div/div/div/div/ul/li[1]/a").click()
    eyes.check_window("homepage_hot_products")

    #homepage_best_Sellers
    driver.find_element_by_xpath("//div[@class='entry-content clearfix']/div[2]/div/div/div/div/div/ul/li[3]/a").click()
    eyes.check_window("homepage_best_Sellers")

    #suits
    driver.find_element_by_xpath("//div[@class='container']/nav/ul/li[2]/a")
    eyes.check_window("suits")

    #shirts
    driver.find_element_by_xpath("//div[@class='container']/nav/ul/li[3]/a")
    eyes.check_window("shirts")

    #pants
    driver.find_element_by_xpath("//div[@class='container']/nav/ul/li[4]/a")
    eyes.check_window("pants")

    #sports coats
    driver.find_element_by_xpath("//div[@class='container']/nav/ul/li[5]/a")
    eyes.check_window("sports_coats")

    #accessories
    driver.find_element_by_xpath("//div[@class='container']/nav/ul/li[6]/a")
    eyes.check_window("accessories")

    #about us
    driver.find_element_by_xpath("//div[@class='container']/nav/ul/li[7]/a")
    eyes.check_window("about us")

    #contact us
    driver.find_element_by_xpath("//div[@class='container']/nav/ul/li[8]/a")
    eyes.check_window("contact us")

    #wishlist
    hover_over_hamburger(driver)
    driver.find_element_by_xpath("//div[@class='menu-bars-item menu-bars-account']/ul/li[1]/a").click()
    eyes.check_window("wishlist")

    #compare
    hover_over_hamburger(driver)
    driver.find_element_by_xpath("//div[@class='menu-bars-item menu-bars-account']/ul/li[2]/a").click()
    eyes.check_window("compare")

    #mycart
    hover_over_hamburger(driver)
    driver.find_element_by_xpath("//div[@class='menu-bars-item menu-bars-account']/ul/li[3]/a").click()
    eyes.check_window("mycart")

    #checkout
    hover_over_hamburger(driver)
    driver.find_element_by_xpath("//div[@class='menu-bars-item menu-bars-account']/ul/li[4]/a").click()
    eyes.check_window("checkout")

    #login/register
    hover_over_hamburger(driver)
    driver.find_element_by_xpath("//div[@class='menu-bars-item menu-bars-account']/ul/li[5]/a").click()
    eyes.check_window("login/register")

    #lost password
    driver.find_element_by_xpath("//div[@class='woocommerce']/form/p[4]/a").click()
    eyes.check_window("lost password")

    #search
    driver.find_element_by_xpath("//li[@class='mini-search']/a/i").click()
    driver.find_element_by_xpath("//input[@class='search-field']").send_keys("suits")
    driver.find_element_by_xpath("//form[@class='woocommerce-product-search searchform']/button/i").click()
    eyes.check_window("search results page")

    #terms and conditions
    driver.find_element_by_xpath("//div[@class='footer-centered']/div/p[3]/a").click()
    eyes.check_window("terms and conditions")
    eyes.close()

except:
    driver.quit()
    eyes.abort_if_not_closed()