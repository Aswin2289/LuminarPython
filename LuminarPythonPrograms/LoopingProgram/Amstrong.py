# Armstrong Number

num=int(input("Enter ur number"))
arm=num
sub=0
sum=0
while(num!=0):
    sub=num%10
    sum=sum+(sub**3)
    num=num//10

print(sum)
if(arm==sum):
    print("Armstrong Number")
else:
    print("Not Armstrong Number")