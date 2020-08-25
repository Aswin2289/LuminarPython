#create a funtion to find factoiral
num=int(input("Enter ur number"))
def fact(num):
    fact=1
    for i in range(1,num+1):
        fact*=i
    return(fact)
data=fact(num)
print(data)

# fu with arg and no return

def fact(num):
    fact=1
    for i in range(1,num+1):
        fact*=i
        print(data)


