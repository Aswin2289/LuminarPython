#first charater is an alphabet and it should be with in a-k

#second should be a digit and it must be divisibe by3

#any number of charater

from re import *
rule='[a-k][369][a-zA-Z0-9]*'
varible=input("Enter ur Variable name")
#fullmatch=to find exact match and reaturn a value otherwise none
matcher=fullmatch(rule,varible)
if(matcher!=None):
    print(varible," is Valid")
else:
    print(varible,"is Invalid")
