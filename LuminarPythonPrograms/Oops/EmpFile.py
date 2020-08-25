import functools
class Person:
    def __init__(self,Eid,Ename,Desig,sal):
        self.Eid=Eid
        self.Ename=Ename
        self.Desig=Desig
        self.sal=int(sal)
    def PrintValues(self):
        print("Emp Id",self.Eid)
        print("Emp name",self.Ename)
        print("Emp Degnation",self.Desig)
        print("Emp salary ",self.sal)
    def __str__(self):
        return self.Ename

f=open("EmpDetails","r")
empl=[]
for data in f:
    data=data.rstrip("\n").split(",")
    Eid=data[0]
    Ename=data[1]
    Desig=data[2]
    sal=data[3]
    obj=Person(Eid,Ename,Desig,sal)
    empl.append(obj)


maxval=functools.reduce(lambda emp:max(sal),empl)
print(maxval)