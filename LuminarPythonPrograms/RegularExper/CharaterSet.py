from re import *
p='[abc]'#check the each charater like a,b,c
p1='[a-z]'#it will check for lowercase a to z charater
p2='[A-Z]'#it will check for all uppercase A to Z charater
p3='[0-9]'#it will check for all nuber to 0 to 9
p4='[A-Za-k]'
p5='[^@-9]'# ^ this symbol mean that expect these values
p6='[^a-zA-z0-9]'#this wil print specail charater

#Prededined  Charaters
p7="\s" #it will check for space
p8="\d" #it will check for digit
p9="\D" #it will check expect all digit
p10="\w"#it will check for all words and numbers expect specal char
p11="\W"#it will check for special charater
match=finditer(p8,"abcacbajdlkancncvavaabc@9")
for i in match:
    print(i.start())
    print(i.group())