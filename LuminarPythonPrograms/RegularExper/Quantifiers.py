#it is used to check the quatitity

import re
p1="a+"#occurance of a ,+ isused tocheck the occurance
p2="a*"#it will check for all a occurance
p3="a?"#it all position of a
p4="a{2}"#it will check only 2 occurances of a
p5="a{2,3}"#it will check min 2 num of a and max 3 num of a
p6="[Kl"
p=re.finditer(p3,"KL38C2280")
count=0
for i in p:
    count+=1
    print(i.start())# to find the position of mtching
    print(i.group())# which object is matching
print("Count",count)