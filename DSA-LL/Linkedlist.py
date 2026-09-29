#adding at  the beginning of ll and find the x in it , find length of ll
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
     
    def count(self): 
        temp=self.head
        l=0  
        while(temp):
            l=l+1
            temp=temp.next
        print("Length : ",l)

    
ll=Linkedlist() 

ll.push(10) 
ll.push(20) 
ll.push(30) 

temp=ll.head 

while(temp): 
    if temp.data==20: 
        print('Yes') 
        break
    temp=temp.next 
else: 
    print('No') 

#length 
# l=0  
# while(temp): 
#     l=l+1 
#     print(l)
#     temp=temp.next  

# print("Length : ",l) 
ll.count()



