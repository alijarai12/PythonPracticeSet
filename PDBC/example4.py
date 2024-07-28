# commit() method is used to commit changes in database
# sql server :- AUTOCOMMIT() is there
# Through python script :- AUTOCOMMIT() is not there

# rollback() method is used to rollback changes in database. It undo the changes if any error occurs

import mysql.connector

try:
    conn = mysql.connector.connect(
        user="root",
        password="root", 
        host="localhost", 
        port=3306,
        database="student"
    )

    if conn.is_connected():
        print("connected")

except Exception as obj:
    print("cannot connect")

cur = conn.cursor()
sql = "INSERT INTO Student(id, name, roll, grade, address) VALUES ('1','ram', 1, 'VI', 'kathmandu')"
cur.execute(sql)
conn.commit()

cur.close()
conn.close()