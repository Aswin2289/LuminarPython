#program to print Fibonacci series

n1=0
n2=1
num=int(input("Enter your Limit"))
i=0
print("Fibonacci series up to",num)
while(i<num):
    print(n1)
    n3=n1+n2
    n1=n2
    n2=n3
    i=i+1