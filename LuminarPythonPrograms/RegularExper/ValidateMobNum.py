from re import *
rule='[0-9]{10}'
n=input("enter mob number")
matcher=fullmatch(rule,n)
if(matcher!=None):
    print("Valid")
else:
    print("Invalid")

