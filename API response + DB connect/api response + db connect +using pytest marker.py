__author__ = 'Roysten'

import MySQLdb as sql
import pytest
import requests
import base64
import json



db = sql.connect("localhost","root","root","test1")
cursor = db.cursor()

@pytest.mark.parametrize("value,state", [('q=','London uk'),('q=','goa india')])

def test_urls_generate(value, state):
    test = state.replace(" ", "+")
    r = requests.get('http://api.openweathermap.org/data/2.5/weather?', params=value+test+"&appid=8cdf78ace3f304f515bccc14d2206017")
    print(r.headers)
    expected_result = r.json()
    print(expected_result)
    json_string = json.dumps(expected_result)
    data = json_format(json_string)
    print(data)
    data_point = data['sys']['country']
    data_point1= data['name']
    expected_result_status_code = r.status_code
    expected_result_encoding = r.encoding
    print(data_point)
    print(data_point1)
    print(expected_result_status_code)
    print(expected_result_encoding)
    status_confirm(expected_result_status_code)


    query1 = """CREATE TABLE COUNTRY (
            COUN  CHAR(20) NOT NULL )"""
    cursor.execute(query1)

    query2 = """INSERT INTO COUNTRY(COUN)
             VALUES (%s))""",data_point
    cursor.execute(query2)
    db.commit()


def json_format(json_string):
    try:
        data = json.loads(json_string)
        print(True)
        return data
    except ValueError:
        print(False)

def status_confirm(expected_result_status_code):
    if expected_result_status_code == 200:
        print('True')
        print(expected_result_status_code)
    else:
        print('False')
        print(expected_result_status_code)





