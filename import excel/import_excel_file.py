__author__ = 'Online'

import csv
import time
from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



driver = webdriver.Firefox()
base_url = 'http://hullforest.managedcoder.com/account/login'

with open('import_data.csv') as csv_file:
   readCSV = csv.reader(csv_file, delimiter=',')
   u = []
   p = []
   for row in readCSV:
       username = row[0]
       password = row[1]
       u.append(username)
       p.append(password)

for i in range(0, len(u)):
   driver.get(base_url)
   element3 = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "input-email")))
   element = driver.find_element(By.ID, "input-email")
   print (u[i])
   element.send_keys(u[i])
   element1 = driver.find_element_by_id("input-password")
   element1.send_keys(p[i])
   print (p[i])
   driver.find_element_by_xpath("//input[@class='btn btn-primary button']").click()
   driver.find_element_by_class_name("secondary-menu-item-2").click()
   i=i+1


driver.quit()