#print A number is primt or not

num=int(input("Enter ur Number"))
flag=0
for i in range(2,num):
    if(num%i==0):
        flag=1
        break
    else:
        flag=0

if(flag==1):
    print("Not prime")
else:
    print("prime")