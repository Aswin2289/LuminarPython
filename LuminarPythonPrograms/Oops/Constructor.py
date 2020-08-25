#Constructor

#its used to initialize instance variable
#constructor automatically invokes during the time of a object cretion
#the name of constructor is always init.(self)

class Employe:
    def __init__(self,Eid,Ename,Desig,Salary):
        self.Eid=Eid
        self.Ename=Ename
        self.Desig=Desig
        self.Salary=Salary
    def PrintEmploye(self):
        print("Your Id is",self.Eid)
        print(self.Ename)
        print(self.Desig)
        print(self.Salary)
ob=Employe(1,"raghu","manager",15000)
ob.PrintEmploye()
print("***********************")
class Person:
    def __init__(self,age,name,gender):
        self.age=age
        self.name=name
        self.gender=gender
    def PrintValues(self):
        print(self.age)
        print(self.gender)
        print(self.name)
obj=Person(27,"male","happy")
obj.PrintValues()