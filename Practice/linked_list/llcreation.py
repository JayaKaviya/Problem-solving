class Node:
   def __init__(self,data):
      self.data=data
      self.next=None 
      
node1=Node(2)
node2=Node(3)
node3=Node(4)

node1.next=node2
node2.next=node3
currenNode=node1

while currenNode:
   print(currenNode.data,end="->")
   currenNode=currenNode.next  
print("null") 


#here curreNode or head=node1 is equal , which is head is just the pointer / reference to the first node of the linked list.
#head.val= 2 (as output)
# head.next = node2 (which is 3 as output)