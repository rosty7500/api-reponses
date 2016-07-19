

from selenium import webdriver
from applitools.eyes import Eyes
import time


def test_non_logged_in_users():
    eyes = Eyes()
    eyes.api_key = 'u51qaFo104ruwwox0ewoWiFZQpijro9Z47fYTk1iQTozU110'

    driver = webdriver.Firefox()
    driver.maximize_window()

    try:
        eyes.open(driver=driver, app_name='Applitools', test_name='TpT Non Logged In Pages')

        # Check HomePage
        driver.get('http://www.teacherspayteachers.com')
        eyes.check_window('Homepage')

        # Check Empty Cart Page
        driver.find_element_by_xpath("//div[@class='drop_down my_cart']/a").click()
        eyes.check_window("Empty Cart Page")
        driver.find_element_by_xpath("//a[@class='common_button green small continue_shopping_button']").click()

        # Check Product Page
        driver.get("https://www.teacherspayteachers.com/Product/Informational-Text-Structures-Task-Cards-1057257")
        eyes.check_window("Product Page")

        # Check cart page with products
        driver.find_element_by_xpath("//div[@class='prod_price_box_wrap']/div[1]/div[2]/div[1]/a").click()
        eyes.check_window("Cart Page")
        driver.find_element_by_xpath("//div[@class='checkout_flow_pages cart_page']/div[1]/div[1]/div[1]/a").click()

        # Check Store Page
        driver.find_element_by_xpath("//div[@class='r_side']/div[3]/div[1]/div[1]/a").click()
        eyes.check_window("Store Page")

        # Check Ratings & Comment Tab on store page
        driver.find_element_by_xpath("//a[@id='ui-id-2']").click()
        time.sleep(2)
        eyes.check_window("Store Page >> Ratings & Comment Tab")

        # Check Gift Cards Page
        driver.find_element_by_xpath("//div[@class='header_user_menu']/a[3]").click()
        eyes.check_window("Gift Card Page")

        # Check Login Page
        driver.find_element_by_class_name("js-login").click()
        eyes.check_window("Login Page")

        # Check Signup Page
        driver.find_element_by_xpath("//div[@class='btns']/a[2]").click()
        eyes.check_window("Signup Page")

        # Check publisher signup page
        driver.find_element_by_xpath("//div[@class='seller_publisher_block']/a").click()
        eyes.check_window("Publisher Signup Page")

        # Terms of Service
        driver.find_element_by_xpath("//div[@class='centered']/a[2]").click()
        eyes.check_window("Terms of service")

        # Privacy Policy
        driver.find_element_by_xpath("//div[@class='centered']/a[3]").click()
        eyes.check_window("Privacy policy")

        # Press
        driver.find_element_by_xpath("//div[@class='block left']/a[4]").click()
        eyes.check_window("Press")

        # Blog
        driver.find_element_by_xpath("//div[@class='block left']/a[5]").click()
        eyes.check_window("Blog")
        driver.back()

        # How to sell items
        driver.find_element_by_xpath("//div[@class='block left']/a[6]").click()
        eyes.check_window("How to sell items")

        # Copyright and trademark policies
        driver.find_element_by_xpath("//div[@class='centered']/a[4]").click()
        eyes.check_window("Copyright and trademark policies")

        # About us
        driver.find_element_by_xpath("//div[@class='centered']/a[5]").click()
        eyes.check_window("About us")

        # Contact us
        driver.find_element_by_xpath("//div[@class='centered']/a[6]").click()
        eyes.check_window("Contact us")

        # Careers
        driver.find_element_by_xpath("//div[@class='centered']/a[7]").click()
        eyes.check_window("Careers")


        #FAQ's and Helps
        driver.find_element_by_xpath("//div[@class='centered']/a[8]").click()
        eyes.check_window("FAQ's and Helps")
        driver.back()

        # Schools
        driver.find_element_by_xpath("//div[@class='header_user_menu']/a[2]").click()
        eyes.check_window("Schools")

        eyes.close()

    finally:
        driver.quit()
        eyes.abort_if_not_closed()