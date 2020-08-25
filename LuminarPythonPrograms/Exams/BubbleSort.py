#program to implement Bubble sort

lst=[]
n=int(input("Enter your limit of list"))
print("Enter your List Elements")
for i in range(0,n):
    lst.append(int(input()))
print("Unsorted list",lst)#[3,2,5]

for i in range(0,n-1):          #i=0,0<2 t                          
    for j in range(0,n-i-1):    #j=0,o<2 t , j=1 1<2 t, j=2 2<2 f
        if(lst[j]>lst[j+1]):    #3>2 t       3>5 f
            temp=lst[j]         #temp=3
            lst[j]=lst[j+1]     #lst[j]=2
            lst[j+1]=temp       #lst[j+1]=3
print("Sorted List is",lst)     #[2,3,5]