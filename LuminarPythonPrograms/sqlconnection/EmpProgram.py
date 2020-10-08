f=open("Empolyeedata")

emp={}
for lines in f:
    data = lines.rstrip("\n").split(",")
    id=data[0]
    name=data[1]
    desg=data[2]
    salary=data[3]
    if(id not in emp):
        emp[id]={"id":id,"name":name,"desg":desg,"salary":salary}

def fatchData(**kwargs):

    id=str(kwargs["id"])
    w=kwargs["prop"]
    if id not in emp:
        print("noite exist")
    else:
        print(emp[id]["name"])
        if "prop" in kwargs:
            print(emp[id][w])





fatchData(id="1001",prop="salary")