f=open("covid_19_india.csv","r")
dict={}
for lines in f:
    # print(lines)
    # break
    data=lines.rstrip("\n").split(",")
    state=data[3]
    cases=data[8]
    #print(state,",",cases)
    if state not in dict:
        dict[state]=cases
    else:
        dict[state] = cases
print(dict)
#or
for k,v in dict.items():
    print(k,",",v)