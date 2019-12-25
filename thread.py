import threading
import time
def print_cube(num):
    for i in range(3):
       time.sleep(1.0)
       print("Cube: {}".format(num * num * num))
  
def print_square(num):
    for i in range(4):
       time.sleep(2.0)
       print("Square: {}".format(num * num))
  
if __name__ == "__main__":
    # creating thread
    t1 = threading.Thread(target=print_square, args=(10,))
    t2 = threading.Thread(target=print_cube, args=(10,))
  
    # starting thread 1
    t1.start()
    # starting thread 2
    t2.start()
  
    # wait until thread 1 is completely executed
    t1.join(10)
    # wait until thread 2 is completely executed
    t2.join(100)
    # wait until thread 1 is completely executed
    t1.join(1000)
    # wait until thread 2 is completely executed
    t2.join(1000000)
  
    # both threads completely executed
    print("Done!")
