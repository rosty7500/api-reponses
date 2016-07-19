__author__ = 'Roysten'

import pytest
from sele
from pages.hullregister1 import register
from pages.hulllogin1 import login
from pages.homepage1 import Homepage
from pages.base_url1 import base_url
import time

register = register()
homepage = Homepage()
login = login()
base_url = base_url()
driver = webdriver.Fire

@pytest.mark.nondestructive
def test_register(base_url, selenium):
    selenium.get(base_url)
    homepage.click_on_create_account(selenium)
    register.register(selenium)
    login.login(selenium)
    time.sleep(10)