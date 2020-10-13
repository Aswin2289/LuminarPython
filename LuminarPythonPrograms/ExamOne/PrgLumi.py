str=input("enter string")
str1=""
for i in range(1,len(str)+1):
    str1+=i*str[i-1]
print(str1)