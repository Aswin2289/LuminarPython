employe={
    "edi":1002,
    "ename":"aswin",
    "desig":"tester",
    "salary":5000,

}

#print employee name
print(employe["ename"])
print("****************************")

#check compnay key is there
print("company" in employe)
print("****************************")

#add a new record company name luminar
employe["company"]="Luminar"
print(employe)
print("****************************")

#update emplyee salary=current salary+5000
employe["salary"]+=5000
print(employe)