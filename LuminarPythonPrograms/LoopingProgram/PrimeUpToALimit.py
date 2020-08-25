#Print prime number up to a limit

low=int(input("Enter ur lower Limit"))#10
upp=int(input("Enter ur lower Limit"))#15
for i in range(low,upp+1):#i=10,i=11
    flag=0 #flag=0,
    for j in range(2,i):#j=2,j=2,j=3
        if(i%j==0):#10%2==0,11%2==0
            flag=1#flag=1,
            break
    if(flag==0):
        print(i)


