#reverse the ll 

class Node: 
    def __init__(self,data): 
        self.data=data 
        self.head=None 

class Linkedlist: 
    def __init__(self): 
        self.head=None 
        
    def push(self,data): 
        new_node=Node(data) 

        new_node.next=self.head 
        self.head=new_node  
     
    def print(self): 
        temp=self.head 
        while(temp): 
            print(temp.data," ") 
            temp=temp.next 
    
    def reverse(self): 

        prev=None 
        current=self.head 
        while(current):  
            next=current.next
            current.next=prev  
            prev=current 
            current=next 
        self.head=prev


    
ll=Linkedlist() 

ll.push(10) 
ll.push(20) 
ll.push(30)   
print('LL elemts:')
ll.print() 
ll.reverse()  
print('LL elemnts after reversing')
ll.print()







