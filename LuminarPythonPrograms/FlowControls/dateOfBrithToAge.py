#enter date of brith and print age

bdate=int(input("enter ur day of brith"))
bmonth=int(input("enter ur month of brith"))
byear=int(input("enter ur year of brith"))

curdate=int(input("enter current date"))
curmonth=int(input("enter current month"))
curyear=int(input("enter current year"))
adate=0
amonth=0
ayear=0
if(curdate<bdate):
    curmonth=curmonth-1
    bdate=bdate+30
else:
    adate=bdate-curdate
if(curmonth<bmonth):
    curyear=curyear-1
    curmonth=curmonth+12
else:
    amonth=curmonth-bmonth
if(curyear-byear>0):
    ayear=curyear-byear
    print("age is", ayear)
else:
   print("age is", ayear)



