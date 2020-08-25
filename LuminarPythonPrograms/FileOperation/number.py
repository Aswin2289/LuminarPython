f=open("numbers","r")
lst=[]
for i in f:
    lst.append(int(i))#or lst.append(num.rstrip("\n"))
print(lst)
sum=0
for i in lst:
    sum=sum+i
print(sum)
#rstrip= used to remove trailing charater
#lstrip= use to remove leading charater
