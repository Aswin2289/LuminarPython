f=open("covid_19_india.csv","r")
dict={}
dict1={}
d={}
totalconfirm=0
totaldeath=0
maxdeath=0
maxcon=0
dlst=[]
clst=[]
for lines in f:
    # print(lines)
    # break
    data=lines.rstrip("\n").split(",")
    state=data[3]
    cases=data[8]
    death=data[7]

    #print(state,",",cases)
    if state not in dict:
        dict[state]=cases

    else:
        dict[state] = cases

    if state not in dict1:
        dict1[state]=death

    else:
        dict1[state] = death

for k,v in dict.items():
    totalconfirm=totalconfirm+int(v)
for k,v in dict1.items():
    totaldeath=totaldeath+int(v)


for k,v in dict1.items():
    dlst.append(int(v))
for k,v in dict1.items():
    if (int(v)==max(dlst)):
        maxdstate=k
        maxdvalue=int(v)
    else:
        pass

for k,v in dict.items():
    clst.append(int(v))

for k,v in dict.items():
    if (int(v)==max(clst)):
        maxcstate=k
        maxcvalue=int(v)
    else:
        pass


print("Total Confirmed Cases in India",totalconfirm)
print("Total Death in India",totaldeath)
print("Maximum death in",maxdstate,"are",maxdvalue)
print("Maximum confirmed State in",maxcstate,"are",maxcvalue)
#or
# for k,v in dict.items():
#     print(k,",",v)