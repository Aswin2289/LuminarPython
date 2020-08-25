

low=int(input("Enter Lower Limit"))
upp=int(input("Enter Upper Limit"))
even=0
odd=0
for i in range(low,(upp+1)):
    if(i%2==0):
        even=even+i
    else:
        odd=odd+i

print("Even Sum:",even)
print("Odd Sum:",odd)