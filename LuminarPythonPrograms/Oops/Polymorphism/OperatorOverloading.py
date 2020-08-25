#operator overloading
class Book:
    def __init__(self,pages):
        self.pages=pages
    def __add__(self, other):
        return Book(self.pages+other.pages)#overiding + operator
    def __sub__(self, other):
        return (self.pages-other.pages)

    def __str__(self):
        return str(self.pages)
ob=Book(100)
ob2=Book(200)
ob1=Book(300)
print(ob+ob1+ob2)

#+operator only work with sring nand integer
#here ob and ob2 are book type
#so we have overide +operator

