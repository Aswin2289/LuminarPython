f=open("covid_19_india.csv","r")
dict={}
d={}
for lines in f:
    data=lines.rstrip("\n").split(",")
    state=data[3]
    death=data[7]
    #print(state,",",cases)
    if state not in dict:
        dict[state]=death
    else:
        dict[state] = death
