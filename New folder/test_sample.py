__author__ = 'BackOffice-3'

import pytest
import requests
from api.main import *


def test_status_confirm(base_url):
    testapi = getapi(base_url)
    data =testapi.to_generate_different_urls()
    if data == 200:
        print(True ,"Status OK - Response ")
    elif data == 401 or data == 403:
        print(False,"Status FAIL - Response ")

def test_get_id(base_url):
    testapi1 =getapi(base_url)
    data1 = testapi1.to_check_id()
    print(data1)
