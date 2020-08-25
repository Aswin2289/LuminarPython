#print max of 3 numbers

num1=int(input("enter ur number1"))
num2=int(input("enter ur number2"))
num3=int(input("enter ur number3"))

if((num1>num2)&(num1>num3)):#(10>20)&(10>30)
    print("max=",num1)
elif((num2>num1)&(num2>num3)):#(20>10)&(20>30)
    print("max=",num2)
elif((num1==num2)&(num2==num3)):
    print(num1,num2,num3,"every number is equal")
else:
    print("max=",num3)