
#To add an element to the list we can use append()

# lst=[]
# lst.append(10)
# print(lst)

even=[]
odd=[]
for i in range(50,100):
    if(i%2==0):
        even.append(i)
    else:
        odd.append(i)

print("even :",even)
print("odd  :",odd)