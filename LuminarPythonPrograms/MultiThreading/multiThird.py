#creating thrwad using cls
from threading import *
import time
class Mythread(Thread):
    def run(self):
        for i in range(1,10):
            time.sleep(1)
            print(i,"\n")
        print(current_thread().getName())
t=Mythread()
t.start()
for i in range(1,10):
    print(i,"\n")
print(current_thread().getName())