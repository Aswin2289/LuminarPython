#Multiple Inheritance


class parent:
    def m1(self):
        print("inside parent1")
class child:
    def m2(self):
        print("inside Child")
class SubChild(child,parent):
    def m3(self):
        print("inside Subchild")

su=SubChild()
su.m1()
su.m2()
su.m3()