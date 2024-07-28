# How to create connection to mysql using python

import mysql.connector

# one way
try:
    conn = mysql.connector.connect(
        user="root",
        password="rooat", 
        host="localhost", 
        port=3306,
    )
except Exception as obj:
    print("cannot connect")

else:
    print("connected")


# other way

config = {
    "user": "root",
    "password": "root", 
    "host": "localhost", 
    "port": 3306,
}

try:
    conn = mysql.connector.connect(**config)
except Exception as obj:
    print("unable to connect")
