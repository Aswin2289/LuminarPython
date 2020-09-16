from threading import *
import time
def display():
    for i in range(1,10):
        time.sleep(2)
        print("child thread executing")
    print(current_thread().getName())
display()
for i in range(1,5):
    print("main thread")
print(current_thread().getName())