#ABABABCAAA print most frequent charater from he string
str="1112222451"
print(str)
dict={}
for i in str:
    if i in dict:
        dict[i]+=1
    else:
        dict[i]=1
print(dict)
result=max(dict,key=dict.get)
print(result)
#ABABABCAA