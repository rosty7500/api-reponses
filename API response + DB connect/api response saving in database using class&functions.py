import requests
import base
import json
import MySQLdb


class db_connection():


    def db_connect(self):
        db = MySQLdb.connect("localhost", "root", "root", "test1")
        cursor = db.cursor()
        return cursor,db


    def test_response(self):
        r = requests.get(base.baseurl + 'weather?q=London,uk&appid='+base.apikey)
        expected_result = r.json()
        json_string = json.dumps(expected_result)
        data = json.loads(json_string)
        data_point = data['sys']['country']
        data_point1= data['name']
        expected_result_status_code = r.status_code
        expected_result_encoding = r.encoding
        data_point = str(data_point)
        print(data_point)
        return data_point


    def query_calling(self):

        query1 = """CREATE TABLE COUNTRY (COUN VARCHAR(20) NOT NULL)"""
        cur.execute(query1)

        sql = "INSERT INTO `test1`.`country`(`COUN`) VALUES ('"+str(data1)+"');"

        cur.execute(sql)
        database.commit()


db = db_connection()
cur,database =db.db_connect()
data1 = db.test_response()
db.query_calling()