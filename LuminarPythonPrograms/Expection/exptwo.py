num1=int(input("Enter ur num1"))
num2=int(input("enter num2"))
try:
    res=num1/num2
    print("result",res)
except Exception as e:
    num1 = int(input("Enter ur num1"))
    num2 = int(input("enter num2"))
    try:
        res = num1 / num2
        print("result", res)
    except Exception as e:
        print(e.args)
finally:
    print("we have a trancation")