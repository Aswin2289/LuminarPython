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

lst=[]
# for emp
# maxval=functools.reduce(lambda emp:max(sal),lst)
# print(maxval)
#reduce can be use in integer value
maxval=list(map(lambda obj:obj.sal,empl))
print(maxval)
m=functools.reduce(lambda sal1,sal2:sal1 if sal1>sal2 else sal2,maxval)
print(m)
maxsal=list(filter(lambda emp:emp.sal==m,empl))
for i in maxsal:
    print(i)