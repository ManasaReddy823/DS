class HashTable:
    def __init__(self):
        self.Max=10
        self.arr= [None for i in range(self.Max)]
        
    def get_hash_key(self,key):
        h=0
        for char in key:
            h += ord(char)
        
        return h%10
    
#     def __getitem__(self,key):
#         h=self.get_hash_key(key)
#         for element in self.arr[h]:
#             if element[0]==key:
#                 value=element[1]
#             else:
#                 
#                 print("key not found")
#         
#         return self.arr[h][0][1]
#         
## with chaining       
#     def __setitem__(self,key,value):
#         h=self.get_hash_key(key)
#         Found= False
#         for idx,element in enumerate(self.arr[h]):
#             if len(element)==2 and element[0]==key:
#                 self.arr[h][idx]=(key,value)
#                 Found=True
#         
#         if not Found:
#             self.arr[h].append((key,value))
#         
#         return self.arr[h]

    def get_prob(self,h):
        return [*range(h,len(self.arr))]+[*range(0,h)]


    def find_slot(self,key,h):
        prob_range=self.get_prob(key,h)
        for index in prob_range:
            if self.arr[index] is None:
                return index
            if self.arr[index]==key:
                return index
            
        raise Exception("Hashmap full")   
            

## with linear probing
    def __setitem__(self,key,value):
        h=self.get_hash_key(key)
        if self.arr[h] is None:
            self.arr[h]=(key,value)
        
        else:
            new_h=self.find_slot(key,h)
            self.arr[new_h]=(key,value)
        print(self.arr)
        
        
    def __getitem__(self,key):
        h=self.get_hash_key(key)
        if self.arr[h] is None:
            return
        prob_range=self.get_prob(h)
        for index in prob_range:
            element=self.arr[index]
            if element is None:
                return
            if element[0]==key:
                return element[1]
        

#                 
#     def __delitem__(self,key):
#         h=self.get_hash_key(key)
#         for ind, element in enumerate(self.arr[h]):
#             if element[0]==key:
#                 del self.arr[h][ind]
#             else:
#                 print("key not found")
#      

 ##linear probing
                 
    def __delitem__(self,key):
        h=self.get_hash_key(key)
        prob_range=self.get_prob(h)
        for index in prob_range:
            element=self.arr[index]
            if element is None:
                return
            if element[0]==key:
                self.arr[index]=None
                
        print(self.arr)
   
        
        
if __name__ == '__main__':
    t=HashTable()
    t["march 17"]=459
    