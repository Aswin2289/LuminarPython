#123=1^3+2^3+3^3

num=int(input("Enter ur number"))
sub=0
sum=0
while(num!=0):
    sub=num%10
    sum=sum+(sub**3)
    num=num//10

print(sum)
