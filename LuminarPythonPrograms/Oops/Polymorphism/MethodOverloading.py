#polymorphism
#manyForms
#Method overloading
#method orverring
#operator overloading

#Method Overloading
#     Same method name but different number of argument
#Method Overloading DoesNot work Directly in Python

class math:
    def add(self):

        num=20
        num2=20
        print(num+num2)
    def add(self,num1):
        num=20
        print("2nd=",num+num1)
    def add(self,num1,num2):
        print("3rd=",num1+num2)

m=math()
m.add(10)
