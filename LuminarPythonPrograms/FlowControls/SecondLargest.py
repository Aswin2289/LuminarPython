#print second largest Number

num1=int(input("enter ur number1"))
num2=int(input("enter ur number2"))
num3=int(input("enter ur number3"))

if((num1>num2)&(num1>num3)):
    if(num2>num3):
        print(num2,"second")
    else:
        print(num3,"second")
elif((num2>num1)&(num2>num3)):
    if(num1>num3):
        print(num1,"second")
    else:
        print(num3,"second")
elif((num3>num1)&(num3>num2)):
    if(num1>num2):
        print(num1,"second")
    else:
        print(num2,"second")
else:
    print("eqal")
