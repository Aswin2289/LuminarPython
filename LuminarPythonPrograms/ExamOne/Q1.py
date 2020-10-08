f=open("QNote","r")
st={}
dict={}
for lines in f:
    data = lines.rstrip("\n").split(",")
    state=data[1]
    total=data[4]
    death=data[5]
    recover=data[6]
    if (state not in st):
        st[state] = {"confirmed": total, "recovered": recover, "death": death}
    else:
        st[state] = {"confirmed": total, "recovered": recover, "death": death}
def fetchData(**kwargs):
    state=kwargs["state"]

    par=kwargs["param"]
    if kwargs["state"] not in st:
        print("Doesnot exist")
    else:

        for k, v in st.items():
            if k==kwargs["state"]:
                print("Total confirmed Cases in ",state,"is",v["confirmed"])
                if "param" in kwargs:
                    if par=="recovered":
                        print("total recovered Cases :", v["recovered"])
                    elif (par == "death"):
                        print("total death Cases :", v["death"])




fetchData(state="Kerala",param="recovered")
