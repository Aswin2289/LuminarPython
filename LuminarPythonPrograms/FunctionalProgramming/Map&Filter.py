#map and Filter

lst=[1,2,3,4]

def square(num):
    return num*num

#map(fuction,itrables)

sq=list(map(square,lst))
print(sq)

#Filter
#filter(funtion,iterable)
def even(num):
    return num%2==0
eve=list(filter(even,lst))
print(eve)

#or using lambda
print("EvEn")

eve=list(filter(lambda num:num%2==0,lst))
print(eve)
print("ODD")
odd=list(filter(lambda num:num%2!=0,lst))
print(odd)

#print all emp ane, in upercase
#print all name have salary >25000
#privide incr 5000for all emp
