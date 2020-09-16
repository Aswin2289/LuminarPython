from threading import *
import time
def square(num):
    for n in num:
        time.sleep(1)
        print(n**2)
def double(num):
    for n in num:
        time.sleep(1)
        print(2*n)
num=[1,2,3,4,5]
begintime=time.time()
print("begin",begintime)
t1=Thread(target=square,args=(num,))
t1.start()
t3=Thread(target=double,args=(num,))
t3.start()
t1.join()
t3.join()
#square(num)
#double(num)
endtime=time.time()
print("end",endtime)
totaltime=endtime-begintime
print("totaltime =",totaltime)