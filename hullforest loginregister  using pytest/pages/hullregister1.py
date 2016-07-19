__author__ = 'Roysten'

from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common import keys
from pages.base_url1 import base_url

class register():
   #_firstname = (By.ID, "input-firstname")
    #_lastname = (By.ID, "input-lastname")
    #_email = (By.ID, "input-email")
    #_address1 = (By.ID, "input-address-1")
    #_input_city = (By.ID, "input-city")
    #_input_country = (By.ID, "input-country")
    #_input_zone = (By.ID, "input-zone")
    #_input_telephone = (By.ID, "input-telephone")
    #_input_confirm_password = (By.ID, "input-confirm")

    base_url()

    def register(self,driver):
        driver.get('http://hullforest.managedcoder.com/account/register')
        element0 = driver.find_element_by_name("custom_field[account][1]")
        element0.click()
        element = driver.find_element_by_id("input-firstname")
        element.send_keys("roystonbseller")
        element1 = driver.find_element_by_id("input-lastname")
        element1.send_keys("fernandes")
        element2 = driver.find_element_by_id("input-email")
        element2.send_keys("roystontestuser@gmail.com")
        element3 = driver.find_element_by_id("input-address-1")
        element3.send_keys("goa")
        element4 = driver.find_element_by_id("input-city")
        element4.send_keys("ponda")
        element5 = Select(driver.find_element_by_id('input-country'))
        element5 = Select(driver.find_element_by_id('input-zone'))
        element6 = driver.find_element_by_id("input-telephone")
        element6.send_keys("8698042639")
        element7 = driver.find_element_by_id("input-password")
        element7.send_keys("rash0207")
        element8 = driver.find_element_by_id("input-confirm")
        element8.send_keys("rash0207")
        element9 = driver.find_element_by_xpath("//div[@class='pull-right']").click()

        element11 = driver.find_element_by_xpath("//div[@class='alert alert-danger warning']").is_displayed()
        print(element11)





