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
#sq=[]
for data in f:
    data=data.rstrip("\n").split(",")
    Eid=data[0]
    Ename=data[1]
    Desig=data[2]
    sal=data[3]
    obj=Person(Eid,Ename,Desig,sal)
    empl.append(obj)
    m=5000
for emp in empl:
    s1=list(map(lambda emp:emp.Ename.upper(),empl))
    #s2=list(filter(lambda emp:emp.sal>25000,empl))
    sq = list(map(lambda emp:emp.sal+m,empl))
s3=list(filter(lambda obj:obj.sal>25000,empl))
print("Name In Upper Case")
for i in s1:
    print(i)
print("Salaru greater than 30000")
for i in s3:
    print(i)
print("Sal increment 5000")
for i in sq:
    print(i)