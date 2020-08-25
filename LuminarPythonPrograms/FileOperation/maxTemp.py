f=open("temparatureData","r")
dict={}
for l in f:
    data=l.rstrip("\n").split(",")
    d=data[0]
    temp=data[1]
    if d not in dict:
        dict[d]=temp
    else:
        old=dict[d]
        if(temp>old):
            dict[d]=temp
print(dict)