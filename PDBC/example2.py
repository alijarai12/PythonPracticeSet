# is_connected() method is used to check connection
# execute() method is used to execute query
# cursor_object.execute(Query, param=None) to execute query

import mysql.connector

try:
    conn = mysql.connector.connect(  # create database connection
    host="localhost",
    user="root",
    passwd="root",
    port=3306
    )

    if conn.is_connected():
        print("connected")

except:
    print("unable to connect")

cur = conn.cursor()  # create cursor object
# cur.execute("CREATE DATABASE Student")  # execute query

cur.execute("SHOW DATABASES")  # execute query

for data in cur:
    print(data[0])

cur.close()

conn.close()
