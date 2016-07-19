__author__ = 'Online'


from selenium import webdriver
from applitools.eyes import Eyes
from selenium.webdriver.common.action_chains import ActionChains
import time


def hover_over_floors(driver):
    floors_dropdown = driver.find_element_by_xpath("//li[@class='drop-down  main-menu-item-2']/a/span")
    ActionChains(driver).move_to_element(floors_dropdown).perform()


def hover_over_sawmill(driver):
    sawmill_dropdown = driver.find_element_by_xpath("//ul[@class='super-menu mobile-menu menu-table']/li[3]/a/span")
    ActionChains(driver).move_to_element(sawmill_dropdown).perform()

def hover_over_forestry(driver):
    forestry_dropdown = driver.find_element_by_xpath("//ul[@class='super-menu mobile-menu menu-table']/li[4]/a/span")
    ActionChains(driver).move_to_element(forestry_dropdown).perform()

def hover_over_floor_second_drop_down(driver):
    time.sleep(5)
    second_dropdown_1 = driver.find_element_by_xpath("//li[@class='drop-down  main-menu-item-2']/a/span")
    ActionChains(driver).move_to_element(second_dropdown_1).perform()
    time.sleep(5)
    second_dropdown_2 = driver.find_element_by_xpath("//ul[@class='super-menu mobile-menu menu-table']/li[2]/ul/li[1]/a")
    ActionChains(driver).move_to_element(second_dropdown_2).perform()

def hover_over_project_second_drop_down(driver):
    time.sleep(5)
    second_dropdown_1 = driver.find_element_by_xpath("//li[@class='drop-down  main-menu-item-2']/a/span")
    ActionChains(driver).move_to_element(second_dropdown_1).perform()
    time.sleep(5)
    second_dropdown_2 = driver.find_element_by_xpath("//ul[@class='super-menu mobile-menu menu-table']/li[2]/ul/li[4]/a")
    ActionChains(driver).move_to_element(second_dropdown_2).perform()


def hover_over_hardwood_lumber_second_drop_down(driver):
    time.sleep(5)
    second_dropdown_1 = driver.find_element_by_xpath("//ul[@class='super-menu mobile-menu menu-table']/li[3]/a/span")
    ActionChains(driver).move_to_element(second_dropdown_1).perform()
    time.sleep(5)
    second_dropdown_2 = driver.find_element_by_xpath("//ul[@class='super-menu mobile-menu menu-table']/li[3]/ul/li[1]/a")
    ActionChains(driver).move_to_element(second_dropdown_2).perform()


def hover_over_biomass_fuel_second_drop_down(driver):
    time.sleep(5)
    second_dropdown_1 = driver.find_element_by_xpath("//ul[@class='super-menu mobile-menu menu-table']/li[3]/a/span")
    ActionChains(driver).move_to_element(second_dropdown_1).perform()
    time.sleep(5)
    second_dropdown_2 = driver.find_element_by_xpath("//ul[@class='super-menu mobile-menu menu-table']/li[3]/ul/li[2]/a")
    ActionChains(driver).move_to_element(second_dropdown_2).perform()

def hover_over_timbers_second_drop_down(driver):
    time.sleep(5)
    second_dropdown_1 = driver.find_element_by_xpath("//ul[@class='super-menu mobile-menu menu-table']/li[3]/a/span")
    ActionChains(driver).move_to_element(second_dropdown_1).perform()
    time.sleep(5)
    second_dropdown_2 = driver.find_element_by_xpath("//ul[@class='super-menu mobile-menu menu-table']/li[3]/ul/li[3]/a")
    ActionChains(driver).move_to_element(second_dropdown_2).perform()

def hover_over_millwork_second_drop_down(driver):
    time.sleep(5)
    second_dropdown_1 = driver.find_element_by_xpath("//ul[@class='super-menu mobile-menu menu-table']/li[3]/a/span")
    ActionChains(driver).move_to_element(second_dropdown_1).perform()
    time.sleep(5)
    second_dropdown_2 = driver.find_element_by_xpath("//ul[@class='super-menu mobile-menu menu-table']/li[3]/ul/li[4]/a")
    ActionChains(driver).move_to_element(second_dropdown_2).perform()

def hover_over_siding_second_drop_down(driver):
    time.sleep(5)
    second_dropdown_1 = driver.find_element_by_xpath("//ul[@class='super-menu mobile-menu menu-table']/li[3]/a/span")
    ActionChains(driver).move_to_element(second_dropdown_1).perform()
    time.sleep(5)
    second_dropdown_2 = driver.find_element_by_xpath("//ul[@class='super-menu mobile-menu menu-table']/li[3]/ul/li[5]/a")
    ActionChains(driver).move_to_element(second_dropdown_2).perform()


def hover_over_recreational_leasing_gallery_second_drop_down(driver):
    time.sleep(5)
    second_dropdown_1 = driver.find_element_by_xpath("//ul[@class='super-menu mobile-menu menu-table']/li[4]/a/span")
    ActionChains(driver).move_to_element(second_dropdown_1).perform()
    time.sleep(5)
    second_dropdown_2 = driver.find_element_by_xpath("//ul[@class='super-menu mobile-menu menu-table']/li[4]/ul/li[6]/a")
    ActionChains(driver).move_to_element(second_dropdown_2).perform()


eyes = Eyes()
eyes.api_key = 'u51qaFo104ruwwox0ewoWiFZQpijro9Z47fYTk1iQTozU110'
driver = webdriver.Firefox()
#driver.maximize_window()

try:
    eyes.open(driver=driver, app_name='hullforest1', test_name='hullforestwhole')

    #Homepage
    driver.get('http://hullforest.managedcoder.com/')
    #eyes.check_window('Homepage')

    #register
    driver.find_element_by_xpath("//a[@class='secondary-menu-item-2']/span").click()
    #eyes.check_window("register")

    # Login
    driver.find_element_by_xpath("//a[@class='secondary-menu-item-1']/span").click()
    # eyes.check_window("login")

    #forgotten password
    driver.find_element_by_xpath("//div[@class='form-group'][2]/a").click()
    # eyes.check_window("forgotten password")

    # Favorite
    driver.find_element_by_xpath("//a[@class='wishlist-total secondary-menu-item-3']/span").click()
    driver.find_element_by_xpath("//div[@class='form-group'][1]/input").send_keys("roystontestuser@gmail.com")
    driver.find_element_by_xpath("//div[@class='form-group'][2]/input").send_keys("12345678")
    driver.find_element_by_xpath("//input[@class='btn btn-primary button']").click()
    # eyes.check_window("Favorite")
    driver.find_element_by_class_name("secondary-menu-item-2").click()

    #cart
    driver.find_element_by_xpath("//a[@class='secondary-menu-item-4']/span").click()
    # eyes.check_window("cart")

    #testimonials
    driver.find_element_by_xpath("//div[@class='row columns ']/div[3]//ul/li[1]/a").click()
    # eyes.check_window("testimonials")

    #the hull story
    driver.find_element_by_xpath("//div[@class='row columns ']/div[3]//ul/li[2]/a").click()
    # eyes.check_window("the hull story")

    #ten reasons to choose hull forest products
    driver.find_element_by_xpath("//div[@class='row columns ']/div[3]//ul/li[3]/a").click()
    # eyes.check_window("ten reasons to choose hull forest products")

    #green certification
    driver.find_element_by_xpath("//div[@class='row columns ']/div[3]//ul/li[4]/a").click()
    # eyes.check_window("green certification")

    #wood is good
    driver.find_element_by_xpath("//div[@class='row columns ']/div[3]//ul/li[5]/a").click()
    # eyes.check_window("wood is good")

    #recreational leasing
    driver.find_element_by_xpath("//div[@class='row columns ']/div[3]//ul/li[6]/a").click()
    # eyes.check_window("recreational leasing")

    #employment
    driver.find_element_by_xpath("//div[@class='row columns ']/div[3]//ul/li[7]/a").click()
    # eyes.check_window("employment")

    #about us
    driver.find_element_by_xpath("//div[@class='row columns ']/div[3]//ul/li[8]/a").click()
    # eyes.check_window("about us")

    #terms and conditions
    driver.find_element_by_xpath("//div[@class='row columns ']/div[3]//ul/li[9]/a").click()
    # eyes.check_window("terms and conditions")

    #contact us
    driver.find_element_by_xpath("//div[@class='row columns ']/div[4]//ul/li[1]/a").click()
    # eyes.check_window("contact us")

    # order history
    driver.find_element_by_xpath("//div[@class='row columns ']/div[4]//ul/li[2]/a").click()
    driver.find_element_by_xpath("//div[@class='form-group'][1]/input").send_keys("roystontestuser@gmail.com")
    driver.find_element_by_xpath("//div[@class='form-group'][2]/input").send_keys("12345678")
    driver.find_element_by_xpath("//input[@class='btn btn-primary button']").click()
    #eyes.check_window("order history")
    driver.find_element_by_class_name("secondary-menu-item-2").click()

    #blog
    driver.find_element_by_xpath("//ul[@class='super-menu mobile-menu menu-table']/li[5]/a").click()
    # eyes.check_window("blog")
    driver.back()

    #wood floors
    hover_over_floors(driver)
    time.sleep(5)
    driver.find_element_by_xpath("//li[@class='drop-down  main-menu-item-2']/a/span").click()
    #eyes.check_window("wood floors")

    #browse our floor
    hover_over_floors(driver)
    time.sleep(5)
    driver.find_element_by_xpath("//ul[@class='super-menu mobile-menu menu-table']/li[2]/ul/li[1]/a").click()
    #eyes.check_window("browse our floor")

    #crafting our wide plank floors
    hover_over_floors(driver)
    time.sleep(5)
    driver.find_element_by_xpath("//li[@class='drop-down  main-menu-item-2']/ul/li[2]/a").click()
    #eyes.check_window("crafting our wide plank floors")

    #guarantee
    hover_over_floors(driver)
    time.sleep(5)
    driver.find_element_by_xpath("//li[@class='drop-down  main-menu-item-2']/ul/li[3]/a").click()
    #eyes.check_window("guarantee")

    #plan your project
    hover_over_floors(driver)
    time.sleep(5)
    driver.find_element_by_xpath("//li[@class='drop-down  main-menu-item-2']/ul/li[4]/a").click()
    #eyes.check_window("plan your project")

    #sawmill
    hover_over_sawmill(driver)
    time.sleep(5)
    driver.find_element_by_xpath("//ul[@class='super-menu mobile-menu menu-table']/li[3]/a/span").click()
    #eyes.check_window("sawmill")

    #hardwood lumber
    hover_over_sawmill(driver)
    time.sleep(5)
    driver.find_element_by_xpath("//ul[@class='super-menu mobile-menu menu-table']/li[3]/ul/li[1]/a").click()
    #eyes.check_window("hardwood lumber")

    #biomass fuel
    hover_over_sawmill(driver)
    time.sleep(5)
    driver.find_element_by_xpath("//ul[@class='super-menu mobile-menu menu-table']/li[3]/ul/li[2]/a").click()
    #eyes.check_window("biomass fuel")

    #Timbers
    hover_over_sawmill(driver)
    time.sleep(5)
    driver.find_element_by_xpath("//ul[@class='super-menu mobile-menu menu-table']/li[3]/ul/li[3]/a").click()
    #eyes.check_window("Timbers")

    #millwork
    hover_over_sawmill(driver)
    time.sleep(5)
    driver.find_element_by_xpath("//ul[@class='super-menu mobile-menu menu-table']/li[3]/ul/li[4]/a").click()
    #eyes.check_window("millwork")

    #siding
    hover_over_sawmill(driver)
    time.sleep(5)
    driver.find_element_by_xpath("//ul[@class='super-menu mobile-menu menu-table']/li[3]/ul/li[5]/a").click()
    #eyes.check_window("siding")

    #bark mulch
    hover_over_sawmill(driver)
    time.sleep(5)
    driver.find_element_by_xpath("//ul[@class='super-menu mobile-menu menu-table']/li[3]/ul/li[6]/a").click()
    #eyes.check_window("bark mulch")

    #sawdust
    hover_over_sawmill(driver)
    time.sleep(5)
    driver.find_element_by_xpath("//ul[@class='super-menu mobile-menu menu-table']/li[3]/ul/li[7]/a").click()
    #eyes.check_window("sawdust")

    #forestry
    hover_over_forestry(driver)
    time.sleep(5)
    driver.find_element_by_xpath("//ul[@class='super-menu mobile-menu menu-table']/li[4]/a/span").click()
    #eyes.check_window("forestry")

     #forestry services
    hover_over_forestry(driver)
    time.sleep(5)
    driver.find_element_by_xpath("//ul[@class='super-menu mobile-menu menu-table']/li[4]/ul/li[1]/a").click()
    #eyes.check_window("forestry services")

     #forestry testimonials
    hover_over_forestry(driver)
    time.sleep(5)
    driver.find_element_by_xpath("//ul[@class='super-menu mobile-menu menu-table']/li[4]/ul/li[2]/a").click()
    #eyes.check_window("forestry testimonials")

    #forest conservation projects
    hover_over_forestry(driver)
    time.sleep(5)
    driver.find_element_by_xpath("//ul[@class='super-menu mobile-menu menu-table']/li[4]/ul/li[3]/a").click()
    #eyes.check_window("forest conservation projects")

    #forestry FAQ
    hover_over_forestry(driver)
    time.sleep(5)
    driver.find_element_by_xpath("//ul[@class='super-menu mobile-menu menu-table']/li[4]/ul/li[4]/a").click()
    #eyes.check_window("forestry FAQ")

    #firewood
    hover_over_forestry(driver)
    time.sleep(5)
    driver.find_element_by_xpath("//ul[@class='super-menu mobile-menu menu-table']/li[4]/ul/li[5]/a").click()
    #eyes.check_window("firewood")

    #recreational leasing
    hover_over_forestry(driver)
    time.sleep(5)
    driver.find_element_by_xpath("//ul[@class='super-menu mobile-menu menu-table']/li[4]/ul/li[6]/a").click()
    #eyes.check_window("recreational leasing")

    #browse by species
    hover_over_floor_second_drop_down(driver)
    driver.find_element_by_xpath("//ul[@class='super-menu mobile-menu menu-table']/li[2]/ul/li[1]/ul/li[1]/a").click()
    #eyes.check_window("browse by species")

    #browse by species > View gallery link (universal)
    driver.find_element_by_xpath("//div[@class='refine-images']/div[1]/div/a[1]").click()
    #eyes.check_window("browse by species > View gallery")

    #View gallery >Product page (universal)
    driver.find_element_by_xpath("//div[@class='gallery-detail-btn']/span/a").click()
    #eyes.check_window("View gallery >Product page")
    time.sleep(5)


    #browse by style
    hover_over_floor_second_drop_down(driver)
    driver.find_element_by_xpath("//ul[@class='super-menu mobile-menu menu-table']/li[2]/ul/li[1]/ul/li[2]/a").click()
    #eyes.check_window("browse by style")

    #browse by style > more info link (universal)
    driver.find_element_by_xpath("//div[@class='refine-images']/div[1]/div[1]/a[2]").click()
    #eyes.check_window("browse by style > more info")

    #browse sale
    hover_over_floor_second_drop_down(driver)
    driver.find_element_by_xpath("//ul[@class='super-menu mobile-menu menu-table']/li[2]/ul/li[1]/ul/li[3]/a").click()
    #eyes.check_window("browse sale")

    #browse related millwork
    hover_over_floor_second_drop_down(driver)
    driver.find_element_by_xpath("//ul[@class='super-menu mobile-menu menu-table']/li[2]/ul/li[1]/ul/li[4]/a").click()
    #eyes.check_window("browse related millwork")

    #shipping
    hover_over_project_second_drop_down(driver)
    driver.find_element_by_xpath("//ul[@class='super-menu mobile-menu menu-table']/li[2]/ul/li[4]/ul/li[1]/a").click()
    #eyes.check_window("shipping")

    #Installation
    hover_over_project_second_drop_down(driver)
    driver.find_element_by_xpath("//ul[@class='super-menu mobile-menu menu-table']/li[2]/ul/li[4]/ul/li[2]/a").click()
    #eyes.check_window("Installation")

    #FAQ
    hover_over_project_second_drop_down(driver)
    driver.find_element_by_xpath("//ul[@class='super-menu mobile-menu menu-table']/li[2]/ul/li[4]/ul/li[3]/a").click()
    #eyes.check_window("FAQ")

    #oak planning
    hover_over_hardwood_lumber_second_drop_down(driver)
    driver.find_element_by_xpath("//ul[@class='super-menu mobile-menu menu-table']/li[3]/ul/li/ul/li[1]/a").click()
    #eyes.check_window("oak planning")

    #FAQ
    hover_over_hardwood_lumber_second_drop_down(driver)
    driver.find_element_by_xpath("//ul[@class='super-menu mobile-menu menu-table']/li[3]/ul/li/ul/li[2]/a").click()
    #eyes.check_window("FAQ")

    #wood chips
    hover_over_biomass_fuel_second_drop_down(driver)
    driver.find_element_by_xpath("//ul[@class='super-menu mobile-menu menu-table']/li[3]/ul/li[2]/ul/li/a").click()
    #eyes.check_window("wood chips")

    #Gallery
    hover_over_timbers_second_drop_down(driver)
    driver.find_element_by_xpath("//ul[@class='super-menu mobile-menu menu-table']/li[3]/ul/li[3]/ul/li[1]/a").click()
    #eyes.check_window("wood chips")

    #FAQ
    hover_over_timbers_second_drop_down(driver)
    driver.find_element_by_xpath("//ul[@class='super-menu mobile-menu menu-table']/li[3]/ul/li[3]/ul/li[2]/a").click()
    #eyes.check_window("FAQ")

    #stairs
    hover_over_millwork_second_drop_down(driver)
    driver.find_element_by_xpath("//ul[@class='super-menu mobile-menu menu-table']/li[3]/ul/li[4]/ul/li[1]/a").click()
    #eyes.check_window("stairs")

    #panelling
    hover_over_millwork_second_drop_down(driver)
    driver.find_element_by_xpath("//ul[@class='super-menu mobile-menu menu-table']/li[3]/ul/li[4]/ul/li[2]/a").click()
    #eyes.check_window("panelling")

    #siding gallery
    hover_over_siding_second_drop_down(driver)
    driver.find_element_by_xpath("//ul[@class='super-menu mobile-menu menu-table']/li[3]/ul/li[5]/ul/li[1]/a").click()
    #eyes.check_window("siding gallery")

    #board and batten
    hover_over_siding_second_drop_down(driver)
    driver.find_element_by_xpath("//ul[@class='super-menu mobile-menu menu-table']/li[3]/ul/li[5]/ul/li[2]/a").click()
    #eyes.check_window("board and batten")

    #recreational leasing gallery
    hover_over_recreational_leasing_gallery_second_drop_down(driver)
    time.sleep(5)
    driver.find_element_by_xpath("//ul[@class='super-menu mobile-menu menu-table']/li[4]/ul/li[6]/ul/li/a").click()
    #eyes.check_window("recreational leasing gallery")


    #My account in max size of the window
    driver.find_element_by_xpath("//a[@class='secondary-menu-item-1']/span").click()
    driver.find_element_by_xpath("//div[@class='form-group'][1]/input").send_keys("roystontestuser@gmail.com")
    driver.find_element_by_xpath("//div[@class='form-group'][2]/input").send_keys("12345678")
    driver.find_element_by_xpath("//input[@class='btn btn-primary button']").click()
    #edit account information
    driver.find_element_by_xpath("//div[@class='content my-account']/ul/li[1]/a").click()
    #eyes.check_window("edit account information")
    driver.back()
    time.sleep(3)
    #change your password
    driver.find_element_by_xpath("//div[@class='content my-account']/ul/li[2]/a").click()
    #eyes.check_window("change your password")
    driver.back()
    time.sleep(3)
    #modify your address book entries
    driver.find_element_by_xpath("//div[@class='content my-account']/ul/li[3]/a").click()
    #eyes.check_window("modify your address book entries")
    driver.back()
    time.sleep(3)
    #downloads
    driver.find_element_by_xpath("//div[@class='content my-orders']/ul/li[2]/a").click()
    #eyes.check_window("downloads")
    driver.back()
    time.sleep(3)
    #your reward points
    driver.find_element_by_xpath("//div[@class='content my-orders']/ul/li[3]/a").click()
    #eyes.check_window("your reward points")
    driver.back()
    time.sleep(3)
    #view your return requests
    driver.find_element_by_xpath("//div[@class='content my-orders']/ul/li[4]/a").click()
    #eyes.check_window("view your return requests")
    driver.back()
    time.sleep(3)
    #your transactions
    driver.find_element_by_xpath("//div[@class='content my-orders']/ul/li[5]/a").click()
    #eyes.check_window("your transactions")
    driver.back()
    time.sleep(3)
    #Recurring payments
    driver.find_element_by_xpath("//div[@class='content my-orders']/ul/li[6]/a").click()
    #eyes.check_window("Recurring payments")
    driver.back()
    time.sleep(3)
    driver.find_element_by_class_name("secondary-menu-item-2").click()

    eyes.close()
finally:
    driver.quit()
    eyes.abort_if_not_closed()