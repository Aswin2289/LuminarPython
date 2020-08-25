#[2,4,6]=[10,8,6]

#[3,5,8]=[13,11,8]

lst=[3,5,8]
# lst1=[]
# f=0
# for i in lst:
#     index=lst.index(i)
#     if(index==0):
#         f=lst[1]+lst[2]
#         lst1.append(f)
#     elif(index==1):
#         f=lst[0]+lst[2]
#         lst1.append(f)
#     elif(index==2):
#         f=lst[0]+lst[1]
#         lst1.append(f)
#     else:
#         break
# print(lst1)

# orrrrr
plst=[]
total=sum(lst)
for element in lst:
    num=total-element
    plst.append(num)
print(plst)


