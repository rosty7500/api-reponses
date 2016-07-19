
from selenium import webdriver
import requests

class base_url():
    def base_url(self):
        driver = webdriver.Firefox()
        driver.get('http://hullforest.managedcoder.com/account/login')

