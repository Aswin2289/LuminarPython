#Definition

dict={}

#values are stored in the form of key, value pairs
#{rolno,ajay}
#key=rolno
#value=ajay
#eg
student={"rol":100,"name":"vishnu","age":25}

#duplicate keys are not allowe


#fetch value
print(student["name"])
print(student["age"])

for key in student:
    print(key,"=",student[key])

#updating value
student["age"]+=10
print(student)
#updating name
student["name"]="aswin"
print(student)
print("****************************")
#adding new key
#-checking a key in the dict
print("total" in student)
print("****************************")
#adding
student["total"]=150
print(student)
