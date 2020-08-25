#exception KeyWords  try and execpt

num1=int(input("Enter num 1"))
num2=int(input("Enter num2"))
lst=[1,2,3]
# res=num1/num2#if num1/0 will terminate upnormally so that is expection
# print("reult",res)

#Sysntax
#try:
    #doubtfull code

#execpt:
    #execption code
#finally:
    #cleanup procestion
try:
    res=num1/num2#if num1/0 will terminate upnormally so that is expection
    pos=int(input("enter ur posiyion"))
    print(lst[pos])
    print("reult",res)

except Exception as e:
    print(e.args)