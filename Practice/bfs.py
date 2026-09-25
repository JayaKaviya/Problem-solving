from collections import deque

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def bfs(root):
     if root==None:
         return 
     
     queue=deque([root])
     
     while queue:
         
         node=queue.popleft()
          
         print(node.data,end="->")
         if node.left:
             queue.append(node.left)
             
         if node.right:
             queue.append(node.right) 
             


root = TreeNode("A")

nodeB = TreeNode("B")
nodeC = TreeNode("C")
nodeD = TreeNode("D")
nodeE = TreeNode("E")
nodeF = TreeNode("F")
nodeG = TreeNode("G")

root.left = nodeB
root.right = nodeC

nodeB.left = nodeD
nodeB.right = nodeE

nodeC.left = nodeF
nodeC.right = nodeG


bfs(root)