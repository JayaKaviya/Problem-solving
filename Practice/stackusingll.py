class Node:
    def __init__(self,val):
        self.val=val
        self.next=None 
        
class Stack:
    
    def __init__(self):
        self.head=None
        self.size=0 

    
    def push(self,data): 
        self.node=Node(data)
        if self.head: 
            self.node.next=self.head 
            self.head=self.node 
        else:
            self.head=self.node 
            
        self.size+=1 
        return self.head   
        
    def pop(self):
        if self.head:
            poppy=self.head 
            self.head=self.head.next
            self.size-=1
            return poppy.val
        else:
            return "stack is empty"
        
    def display(self):      
        curr=self.head       
        while curr:
            print(curr.val,end="->")
            curr=curr.next 
            
    def sizee(self):
        return self.size 
        
        
s=Stack() 
s.push('A') 
s.push('B') 

s.display()

print("Pop: ", s.pop()) 
print("Size: ", s.sizee())
            
        

