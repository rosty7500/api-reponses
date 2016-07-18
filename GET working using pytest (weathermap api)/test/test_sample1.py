import pytest
import requests
from api.main import *

@pytest.mark.country
def test_data_present(baseurl,urlparam):
    values = ['sys', 'dt', 'base', 'weather', 'wind', 'name', 'main', 'clouds', 'id', 'cod', 'coord']
    testapi = getapi(baseurl,urlparam)
    data=testapi.to_store_reponse()
    for i in values:
        if i in data:
            print("Yes!, I'm Present")
        else:
            print("No!, I'm not Present")

@pytest.mark.country
def test_confirm_status(baseurl,urlparam):
    testapi1 = getapi(baseurl,urlparam)
    data1 = testapi1.to_generate_different_urls()
    if data1 == 200:
        print(True ,"Status OK - Response ")
        print(data1)
    elif data1 == 401 or data1 == 403:
        print(False,"Status FAIL - Response ")
        print(data1)

@pytest.mark.country
def test_url_return(baseurl,urlparam):
    testapi2 = getapi(baseurl,urlparam)
    data2 = testapi2.validate_params()
    print(data2)

@pytest.mark.country
def test_validate_country(baseurl,urlparam):
    testapi3 = getapi(baseurl,urlparam)
    data3 = testapi3.validate_country()
    if data3 == 'GB' or data3 == "IN":
        print("Country is present",data3)
    else:
        print("Country is missing")


@pytest.mark.lonlat
def test_validate_lonlat(baseurl,urlparam):
    testapi4 = getapi(baseurl,urlparam)
    data4 = testapi4.validate_lonlat()
    print(data4)

@pytest.mark.country
def test_validate_state(baseurl,urlparam):
    testapi5 = getapi(baseurl,urlparam)
    data5 = testapi5.validate_location()
    print("The State is present :", data5)