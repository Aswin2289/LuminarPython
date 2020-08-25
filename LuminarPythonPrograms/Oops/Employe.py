class Employe:
    def setEmploye(self,Eid,Ename,Desig,Salary):
        self.Eid=Eid
        self.Ename=Ename
        self.Desig=Desig
        self.Salary=Salary
    def PrintEmploye(self):
        print("Your Id is",self.Eid)
        print(self.Ename)
        print(self.Desig)
        print(self.Salary)
ob=Employe()
ob.setEmploye(1,"raghu","manager",15000)
ob.PrintEmploye()
