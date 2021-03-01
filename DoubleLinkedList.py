class Node:
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev
        
    
class DoubleLinkedList():
    def __init__(self):
        self.head=None
        
    def print_forward(self):
    # This method prints list in forward direction. Use node.next
        if self.head is None:
            print("Linked list is empty")
            return
        itr = self.head
        llstr = ''
        while itr:
            llstr += str(itr.data)+' --> ' if itr.next else str(itr.data)
            itr = itr.next
        print(llstr)
    
    def print_backward(self):
    # Print linked list in reverse direction. Use node.prev for this.
        if self.head is None:
            print("Linked list is empty")
            return
        
        itr = self.head
        while itr.next:
            itr=itr.next
            
        llstr = ''
        while itr:
            llstr += str(itr.data)+' --> '
            itr = itr.prev
        
        print(llstr)
    
    def insert_at_begining(self, data):
        if self.head is None:
            node = Node(data, self.head, None)
            self.head = node
        
        else:
            node = Node(data, self.head, None)
            self.head.prev=node
            self.head= node
        
        
   
    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data,None,None)
            return
    

        itr = self.head

        while itr.next:
            itr = itr.next
        
        
        itr.next = Node(data,None,itr)
        

if __name__ == '__main__':
    ll = DoubleLinkedList()
    ll.insert_at_begining(5)
    ll.insert_at_begining(6)
    ll.insert_at_end(4)
    ll.insert_at_end(10)
    ll.print_forward()
    ll.print_backward()
