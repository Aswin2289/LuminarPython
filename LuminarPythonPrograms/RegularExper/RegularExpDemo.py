# it is used for pattern matching

#Step1  we have to import re module
import re

p=re.finditer("ab","ab aba baba babababababbababab")
count=0
for i in p:
    count+=1
    print(i.start())# to find the position of mtching
    print(i.group())# which object is matching
print("Count",count)