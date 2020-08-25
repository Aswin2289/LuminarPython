#Object Oriented programming

##key concept

#1 Class
#2 objects
#3refrence

#1 class=plan,design,blueprint,template

#2object= real world entity

#3Reference=to do a work over object

#Class Syntax

#class classname:
#   variables
#   method
#eg
#step 1 create a class
class Person:
    def setValues(self,age,name,gender):
        self.age=age
        self.name=name
        self.gender=gender
    def PrintValues(self):
        print(self.age)
        print(self.gender)
        print(self.name)
#step 2 create an object
#objetname=classname
obj=Person()    #obj is a reference of classs person

#self is a keywork to point current class instance variable

