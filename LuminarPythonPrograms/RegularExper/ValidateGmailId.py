from re import *
gm=input("Enter ur gmail id")
rule='[a-zA-Z0-9]+[@][g][m][a][i][l][.][c][o][m]'
matcher=fullmatch(rule,gm)
if(matcher!=None):
    print("Valid")
else:
    print("Invalid")
