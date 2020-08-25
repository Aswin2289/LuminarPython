f=open("covid_19_india.csv","r")
dict={}
for lines in f:
    # print(lines)
    # break
    data=lines.rstrip("\n").split(",")
    state=data[3]
    death=data[7]
    #print(state,",",cases)
    if state not in dict:
        dict[state]=death
    else:
        dict[state] = death

for k,v in dict.items():
    print(k,",",v)

#print which state has highest dear=th rate
#hightet confirmes cases
#calclate total no. of confirmes cases
#total number of  death in india