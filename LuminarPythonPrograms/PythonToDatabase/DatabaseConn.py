import mysql.connector
db=mysql.connector.connect(
    host="localhost",
    port=3307,
    user="root",

    password="Password@123",
    auth_plugin='mysql_native_password'

    )
