class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
    
node1 = Node(3)
node2 = Node(5)
node3 = Node(13)
node4 = Node(2)

node1.next=node2

node2.prev=node1
node2.next=node3

node3.prev=node2
node3.next=node4 

node4.prev=node3 

c1=node1 
while c1:
  print(c1.data,end="->")
  c1=c1.next 
print("null")
  
c2=node4
while c2:
  print(c2.data,end="->")
  c2=c2.prev
print("null")