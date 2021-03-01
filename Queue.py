'''
Created on 02-Jan-2021

@author: manas
'''
from collections import deque
import time
import threading

class Queue:
    
    def __init__(self):
        self.buffer = deque()
  
    
    def enqueue(self, val):
        self.buffer.appendleft(val)
        
    def dequeue(self):
        print(self.buffer.pop())
    
    def is_empty(self):
        return len(self.buffer)==0
    
    def size(self):
        return len(self.buffer)

if __name__ == '__main__':
    pq = Queue()

    arr = ['pizza','samosa','pasta','biryani','burger']
    
    t = time.time()
    
    def add_orders(i):
        for value in i:
            pq.enqueue(value)
            time.sleep(0.5)
            
    def remove_orders():
        while True:
            pq.dequeue()
            time.sleep(2)
    
    t1= threading.Thread(target=add_orders, args=(arr,))
    time.sleep(1)
    t2= threading.Thread(target=remove_orders,args=())
    
    t1.start()
    t2.start()

    