__author__ = 'Roysten'

from selenium.webdriver.common.by import By

class Homepage(object):
    _create_account_link = (By.XPATH, "//a[@class='secondary-menu-item-2']/span")

    def click_on_create_account(self, driver):
        driver.find_element(*self._create_account_link).click()