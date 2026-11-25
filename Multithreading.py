
import time

import threading

def square(num1):
    sq = num1**2
    print("Square function start")
    time.sleep(1)
    print(sq)

def cube(num2):
    cu = num2**3
    print("Cube function start")
    time.sleep(1)
    print(cu)

s1 = threading.Thread(target=square,args=[10])
c1 = threading.Thread(target=cube,args=[12])

s1.start() # to start thread
c1.start()

print(s1.getName()) # <bound method Thread.getName of <Thread(Thread-1 (square), started 13056)>>
print(s1.ident) # to print thread ID
print(s1.native_id) # to print thread ID
print(s1.is_alive()) # to find thread is start or not
print(s1.run()) # Not for use internally start.
print(s1.setName("number square"))
print(f"After setname :{s1.getName()})")

s1.join() # to end thread
c1.join()

print("Operation Completed")
