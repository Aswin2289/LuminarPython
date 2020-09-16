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
sql="""INSERT INTO EMPLOYEE(
    FIRST_NAME,
    LAST_NAME,
    AGE,
    SEX,
    INCOME) VALUES ('janko','man','25','M','20000')"""
try:

    cursor.execute(sql)
    db.commit()
except Exception as e:
    db.rollback()
    print(e.args)
finally:
    db.close()
