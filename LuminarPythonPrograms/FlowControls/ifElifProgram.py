#elif program
#   Syntax
#==============


#if(condition):
#   stmt
#elif(condition):
#    stmt
#else:
#    stmt

#============================

num1=int(input("enter ur number1"))
num2=int(input("enter ur number2"))

if(num1>num2):
    print(num1,"is larger")
elif(num1==num2):
    print(num1,num2,"are equal")
else:
    print(num2,"is larger")
