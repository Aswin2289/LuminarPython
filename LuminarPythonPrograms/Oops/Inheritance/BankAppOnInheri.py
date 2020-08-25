class Person:
    def setValue(self,pname,age):
        self.pname=pname
        self.age=age
    def printValue1(self):
        print("Ur Name Is",self.pname)
        print("ur Age is",self.age)
class Bank(Person):
    bname="SBI"
    def __init__(self,accno,balance):
        self.accno=accno

        self.balance=balance

    def PrintValues(self):
        print("Yout AccountNo",self.accno)

        print("your Balance",self.balance)
        print("your bank",self.bname)
    def WithDraw(self):

        print("Your Total amount=",self.balance)
        num = int(input("Enter your Amount you want to withdraw"))
        if(num>self.balance):
            print("Withdrawal Not Possible")
        else:
            self.balance=self.balance-num
            print("Your Current Balance=",self.balance)
    def Deposit(self):

        self.num = int(input("Enter your Amount you want to Deposit"))
        self.balance+=self.num


Accno=int(input("Enter your Accno"))
name=input("Enter your Name")
Balance=1000

age=int(input("Enter Age"))
obj=Bank(Accno,Balance)
obj.setValue(name,age)
i=1
print("1.Account Details")
print("2.Deposit Amount")
print("3.Withdraw")
print("4.Exit")
i=int(input("Enter ur choice"))
while(i<4):

    if(i==1):
        obj.PrintValues()
        obj.printValue1()
    elif(i==2):
        obj.Deposit()
    elif(i==3):
        obj.WithDraw()
    else:
        break
    i=int(input("Enter ur choice"))