l=3

lst=[]
print("Enter your List Elements")
for i in range(0,l):
    #print("Enter ur list ")
    lst.append(int(input()))
f=0
lst1=[]
m=len(lst)-1
for i in range(0,m):
    num=lst[i],lst[i+1]
    if num not in lst1:
        lst1.append(num)
    num1=lst[0],lst[m]
    if num1 not in lst1:
        lst1.append(num1)
print(lst1)




