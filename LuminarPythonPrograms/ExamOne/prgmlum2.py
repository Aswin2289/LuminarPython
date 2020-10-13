lst1=[]
lst2=[]
print("enter 5 numbers")
for i in range (0,5):
    num=int(input())
    lst1.append(num)
for j in range(0,len(lst1)):
    if lst1[j]<5:
        lst2.append(lst1[j]-1)
    elif lst1[j]>5:
        lst2.append(lst1[j] + 1)
    else:
        lst2.append(lst1[j])

print("UR numbers are:",lst1)
print("result is:",lst2)


res=[x+1 if x>5 else x-1 for x in lst1]
print(res)