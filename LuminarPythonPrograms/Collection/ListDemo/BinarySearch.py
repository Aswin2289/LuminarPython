# Search a element using binary

#steps
# 1. sort the array
# 2. set lower and upper limit
# 3. mid claculate and check mid== element

lst=[]
num=int(input("Enter your limit of list"))
print("Enter your List Elements")
for i in range(0,num):
    lst.append(int(input()))

lst.sort()
print(lst)
n=int(input("Enter ur element to be searched"))
low=0
upp=len(lst)-1
flag=0
while(low<=upp):
    mid=(low+upp)//2
    if(n>lst[mid]):
        low=mid+1
    elif(n<lst[mid]):
        upp=mid-1
    elif(n==lst[mid]):
        flag+=1
        break
    else:
        print("element not exist")

if(flag>0):
    print("element found at position",mid)

