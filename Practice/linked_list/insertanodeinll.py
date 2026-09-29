#insert at pos 2

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
    
def insert(h,node,pos):
    
    if h is None:
        return node
        
    curr=h
    for i in range(pos-2):
        curr=curr.next 
        
    node.next=curr.next 
    curr.next=node
        
      
node1 = Node(7)
node2 = Node(11)
node3 = Node(3)
node4 = Node(2)
node5 = Node(9)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

newnode=Node(97)
display(node1)   
insert(node1,newnode,2)
display(node1)
        