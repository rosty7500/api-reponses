__author__ = 'Roysten'

import MySQLdb as sql
#db_connect()
db = sql.connect("localhost","root","root","test")
cursor = db.cursor()


query = "SELECT VERSION()"
cursor.execute(query)
result = cursor.fetchone()
print"Database version : %s " % result

'''
query1 = """CREATE TABLE CUSTOMER (
         FIRST_NAME  CHAR(20) NOT NULL,
         LAST_NAME  CHAR(20),
         AGE INT,
         SEX CHAR(1),
         INCOME FLOAT,
         ID INT )"""
cursor.execute(query1)

query2 = """CREATE TABLE EMPLOYEE (
         FIRST_NAME  CHAR(20) NOT NULL,
         LAST_NAME  CHAR(20),
         AGE INT,
         SEX CHAR(1),
         INCOME FLOAT,
         ID INT )"""
cursor.execute(query2)'''

query3 = """INSERT INTO EMPLOYEE(FIRST_NAME,
         LAST_NAME, AGE, SEX, INCOME)
         VALUES ('Mac', 'Mohan', 21, 'M', 2000)"""
cursor.execute(query3)
db.commit()

query5 = """INSERT INTO EMPLOYEE(FIRST_NAME,
         LAST_NAME, AGE, SEX, INCOME)
         VALUES ('royston', 'fernandes', 31, 'M', 10)"""
cursor.execute(query5)
db.commit()

query4 ="SELECT * FROM EMPLOYEE"
cursor.execute(query4)
result4 = cursor.fetchall()
for row in result4:
      fname = row[0]
      lname = row[1]
      age = row[2]
      sex = row[3]
      income = row[4]
      id = row[5]
      print ("fname=%s,lname=%s,age=%d,sex=%s,income=%d,id=%d" %(fname, lname, age, sex, income, id))
cursor.execute("SELECT COUNT(*) FROM EMPLOYEE")
print cursor.fetchall()
db.close()