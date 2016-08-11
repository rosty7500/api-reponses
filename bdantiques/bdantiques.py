__author__ = 'BackOffice-3'


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from urllib.request import urlretrieve
import urllib
import os
import time
import pytest
import csv
from selenium.common.exceptions import NoSuchElementException


driver = webdriver.Firefox()
with open('antiques1.csv') as csv_file:
   readCSV = csv.reader(csv_file, delimiter=',')
   names = []
   for row in readCSV:
       n = row[0]
       names.append(n)

driver.get("http://bdantiques.com/")
