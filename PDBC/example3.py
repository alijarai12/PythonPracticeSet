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
cur.execute("Use student")
# cur.execute("""Create Table Student(
#             id int primary key, 
#             name varchar(100),
#             roll int,
#             grade varchar(10),
#             address varchar(100)
#             )""")

cur.execute("DESC Student")
for data in cur:
    print(data)

cur.close()
conn.close()