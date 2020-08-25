lst=[2,3,4,5]
ele=int(input("enter ur element"))
#j=len(lst)
for i in lst:
    for j in lst:
        if(i+j==ele):
            print(i,j)
        else:
            pass