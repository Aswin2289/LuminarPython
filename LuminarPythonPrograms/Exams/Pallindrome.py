#Check a Sequance is pallindrome or note


n=int(input("Enter number:"))
temp=n
pal=0
while(n>0):
    num=n%10
    pal=pal*10+num
    n=n//10
if(temp==pal):
    print("The number is a palindrome")
else:
    print("The number is Not a palindrome")