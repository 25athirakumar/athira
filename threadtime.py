import threading
import time
def print_cube(num):
    print("Cube: {}".format(num * num * num))
  
def print_square(num):
    print("Square: {}".format(num * num))
  
if __name__ == "__main__":
    # creating thread
    t1 = threading.Thread(target=print_square, args=(10,))
    t2 = threading.Thread(target=print_cube, args=(10,))
  
    # starting thread 1
    t1.start()
    time.sleep(1.0)
    if t1.is_alive():
       print("still running")
    else:
       print("dead")
    # starting thread 2
    t2.start()
    time.sleep(2.0)
    # wait until thread 1 is completely executed
    t1.join()
    # wait until thread 2 is completely executed
    t2.join()
    
    # both threads completely executed
    print("Done!")
