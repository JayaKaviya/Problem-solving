class Node:
    def __init__(self,val):
        self.val=val
        self.next=None 
        
def display(node):      
    curr=node      
    while curr:
        print(curr.val,end="->")
        curr=curr.next 
    print("None")
    print() 
    
def delte(h,node):
    
    if h==node:
        return h.next 
    curr=h
    
    while curr and curr.next!=node:
        curr=curr.next 
        
    curr.next=curr.next.next 
        
      
node1 = Node(7)
node2 = Node(11)
node3 = Node(3)
node4 = Node(2)
node5 = Node(9)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5


display(node1)   
delte(node1,node5)
display(node1)
        