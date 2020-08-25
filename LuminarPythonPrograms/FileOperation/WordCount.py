f=open("Words","r")
dict={}
for lines in f:
    words=lines.rstrip("\n").split(" ")
    for w in words:
        if w not in dict:
            dict[w] = 1
        else:
            dict[w]+=1
for k,v in dict.items():
    print(k,",",v)
