class Node:
    def __init__(self,val):
        self.val=val
        self.next=None 
        
class Stack:
    
    def __init__(self):
        self.front=None
        self.rear=None
        self.size=0 

    
    def push(self,data): 
        self.node=Node(data)
        if self.rear:
            self.rear.next=self.node
            self.rear=self.node
        else:
            self.rear=self.front=self.node
            
        self.size+=1   
        
    def pop(self):
        if self.front:
            poppy=self.front 
            self.front=self.front.next
            self.size-=1
            return poppy.val
        else:
            return "stack is empty"
        
    def display(self):      
        curr=self.front       
        while curr:
            print(curr.val,end="->")
            curr=curr.next 
        print("None")
        print()
            
    def sizee(self):
        return self.size 
        
        
s=Stack() 
s.push('A') 
s.push('B') 

s.display()

print("Pop: ", s.pop()) 
print("Size: ", s.sizee())
            
        


