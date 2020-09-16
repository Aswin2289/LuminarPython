import mysql.connector
db=mysql.connector.connect(
    host="localhost",
    port=3307,
    user="root",

    password="Password@123",
    database="luminarpython" ,
    auth_plugin='mysql_native_password'

    )
cursor=db.cursor()
try:
    sql="SELECT * FROM EMPLOYEE"
    cursor.execute(sql)
    myresult=cursor.fetchall()
    for x in myresult:
        print(x)
except Exception as e:
    db.rollback()
    print(e.args)
finally:
    db.close()