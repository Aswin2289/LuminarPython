#step 1= import mysqlconntor

import mysql.connector
# establish connetion

db=mysql.connector.connect(
    host="localhost",
    port=3307,
    user="root",

    password="Password@123",
    auth_plugin='mysql_native_password'

    )
#create a cursor object ,
# object that carrys data to mysql visversa
cursor=db.cursor()

#execute mysql querys using execute() method

sql="SELECT VERSION()"

cursor.execute(sql)
#fatch a single row using fatchone() methon


data=cursor.fetchone()
print("database Version:",data)

# disconnect from server
db.close()

#ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY 'Password@123';




