import mysql.connector
import pandas as pd
import sys
class DBhelper:
    def __init__(self):
        try:
            self.conn=mysql.connector.connect(host="localhost",user="root",password="",database="first")
            self.mycursor=self.conn.cursor()
        except:
            print("Some error occured Could not connect to database")
            sys.exit(0)
        else:
            print("connected to Database")
    def register(self,name,emai,password):
        try:
            self.mycursor.execute("""INSERT INTO `user` (`id`, `name`, `emai`, `password`) 
            VALUES (NULL, '{}', '{}', '{}');""".format(name,emai,password))
            self.conn.commit()
        except:
            return -1
        else:
            return 1
    def search(self,emai,password):
        self.mycursor.execute("""SELECT * FROM user WHERE emai LIKE '{}' AND 
        password LIKE '{}' """.format(emai,password))
        data=self.mycursor.fetchall()
        print(data)
"""conn=mysql.connector.connect(host='localhost',user='root',password='',database='world')
x=pd.read_sql_query("SELECT * FROM city",conn)
print(x)"""

