class Queue:

  #Constructor creates a list
  def __init__(self):
      self.queue = list()

  #Adding elements to queue
  def enqueue(self,data):
      #Checking to avoid duplicate entry (not mandatory)
      if data not in self.queue:
          self.queue.insert(0,data)
          return True
      return False

  #Removing the last element from the queue
  def dequeue(self):
      if len(self.queue)>0:
          return self.queue.pop()
      return ("Queue Empty!")

  #Getting the size of the queue
  def size(self):
      return len(self.queue)

  #printing the elements of the queue
  def printQueue(self):
      return self.queue

myQueue = Queue()
print(myQueue.enqueue(int(input("enter no.to enqueue")))) 
print(myQueue.enqueue(int(input("enter no.to enqueue"))))
print(myQueue.enqueue(int(input("enter no.to enqueue"))))
print(myQueue.enqueue(int(input("enter no.to enqueue"))))
print(myQueue.enqueue(int(input("enter no.to enqueue"))))
print(myQueue.enqueue(int(input("enter no.to enqueue"))))
print(myQueue.enqueue(int(input("enter no.to enqueue"))))
print(myQueue.enqueue(int(input("enter no.to enqueue"))))
print(myQueue.enqueue(int(input("enter no.to enqueue"))))
print(myQueue.size())     
print(myQueue.dequeue())  
print(myQueue.dequeue())  
print(myQueue.dequeue())  
print(myQueue.dequeue())  
print(myQueue.size())     
print(myQueue.dequeue())  