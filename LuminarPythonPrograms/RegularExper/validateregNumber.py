from re import *
f=open("Regno","r")
lst=[]
for data in f:
    data = data.rstrip("\n")
    rule = '[K][L][0-9]{2}[A-Z]{1,2}[0-9]{4}'
    matcher = fullmatch(rule, data)
    if (matcher != None):
        lst.append(data)
    else:
       pass
print(lst)
