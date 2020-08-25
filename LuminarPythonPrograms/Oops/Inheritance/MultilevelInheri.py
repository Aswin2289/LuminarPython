#MultiLevel Inheritance

class parent:
    def m1(self):
        print("inside parent1")
class child(parent):
    def m2(self):
        print("inside Child")
class SubChild(child):
    def m3(self):
        print("inside Subchild")
#invoking only possible from derived to base
su=SubChild()
su.m1()
su.m2()
su.m3()