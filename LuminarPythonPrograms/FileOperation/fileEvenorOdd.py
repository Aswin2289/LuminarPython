f=open("numbers","r")
lst=[]
for i in f:
    lst.append(int(i))
#print(lst)
even=[]
odd=[]
for i in lst:
    if(i%2==0):
        even.append(i)
    else:
        odd.append(i)
print(even)
print("**************************")
print(odd)