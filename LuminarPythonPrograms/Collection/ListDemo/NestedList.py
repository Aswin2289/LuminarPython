employee=[[1001,"arjun",15000],
        [1002,"aswin",25000],
          [1003,"jack",5000]]
# for employe in employee:
#     print(employe)
# for employe in employee:
#     print(employe[1])

# for emp in employee:
#     if(emp[2]>17000):
#         print(emp[1])
sum=0
for emp in employee:
    sum=sum+emp[2]
print(sum)