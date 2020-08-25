#Slicing Operation
lst=[1,2,3,4,5,6,7,8,9,10]
# print(lst[-1])
# print(lst[1:5])
elm=int(input("Enter your element"))
flg=0
for i in lst:
    if(i==elm):
        flg=1
        break
    else:
        flg=0

if(flg==1):
    print("item found",elm)
else:
    print("item not found",elm)