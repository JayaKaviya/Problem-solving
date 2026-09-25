#dfs by stack, iteration method

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def dfs(root):
     if root==None:
         return 
     
     stack=[root]
     
     while stack:
         
         node=stack.pop()
          
         print(node.data,end="->")
         if node.right:
             stack.append(node.right)
             
         if node.left:
             stack.append(node.left) 
             


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


dfs(root)