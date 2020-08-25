#method overriding

class Parent:
    def phone(self):
        print("Have samsung")
class child(Parent):
    def phone(self):
        print("iphone")
c=child()
c.phone()
print("*********************")
class Employee:
    def __init__(self,eid,name,sal):
        self.eid=eid
        self.name=name
        self.sal=sal
    def printVal(self):
        print(self.eid)
        print(self.name)
        print(self.sal)

    def __str__(self):
        return self.name
obj=Employee(100,"ajay",25000)
obj1=Employee(101,"pjay",30000)
obj2=Employee(102,"hjay",35000)
obj3=Employee(102,"jjay",45000)
ls=[]
ls.append(obj)
ls.append(obj1)
ls.append(obj2)
ls.append(obj3)
for i in ls:
    if(i.sal>32000):
        print(i)
#print(obj)