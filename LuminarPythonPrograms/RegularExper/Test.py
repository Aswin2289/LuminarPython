from re import *
f=open("TESTFILE","r")
lst=[]
lst1=[]
for lines in f:
    data = lines.rstrip("\n").split(",")
    email=data[3]
    phno = data[2]
    if (email!=None and phno!=None):
        rule = '[a-zA-Z0-9]+[@][g][m][a][i][l][.][c][o][m]'
        rule1 = '[0-9]{10}'
        matcher = fullmatch(rule, email)
        matcher1=fullmatch(rule1,phno)
        if (matcher != None and matcher1!=None):
            lst.append(lines.rstrip("\n"))
        else:
            lst1.append(lines.rstrip("\n"))
    else:
        pass
print("Valid datas")
print(lst)
print("Invalid Datas")
print(lst1)