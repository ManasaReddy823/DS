from collections import deque

class Stack:
    def __init__(self):
        self.container = deque()
    
    def push(self,val):
        self.container.append(val)
        
    def pop(self):
        return self.container.pop()
    
    def peek(self):
        return  self.container[-1]
    
    def is_empty(self):
        return len(self.container)==0
    
    def size(self):
        return len(self.container)
    
    
def reverse_string(string_rev):
    stack=Stack()
    for i in string_rev:
        stack.push(i)
        
    rev_str=""
    while stack.size()!=0:
        rev_str += stack.pop()

    return rev_str

def is_balanced(string_rev):
    stack=Stack()
    for i in string_rev:
        stack.push(i)
        
    for i in range(stack.size()):
        print(stack.peek())
        
            
            
    

if __name__ == '__main__':
    is_balanced("({a+b})")
    
    