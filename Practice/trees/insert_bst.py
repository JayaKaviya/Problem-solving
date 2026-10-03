class TreeNode:
  def __init__(self, data):
    self.data = data
    self.left = None
    self.right = None

def insert(root, data):
    
    if root is None:
        return TreeNode(data)
    
    if data<root.data:
        root.left=insert(root.left,data)
        
    elif data> root.data:
        root.right=insert(root.right,data)
    
    return root
        

def inOrderTraversal(node):
  if node is None:
    return
  inOrderTraversal(node.left)
  print(node.data, end=", ")
  inOrderTraversal(node.right)

root = TreeNode(13)
node7 = TreeNode(7)
node15 = TreeNode(15)
node3 = TreeNode(3)
node8 = TreeNode(8)
node14 = TreeNode(14)
node19 = TreeNode(19)
node18 = TreeNode(18)

root.left = node7
root.right = node15

node7.left = node3
node7.right = node8

node15.left = node14
node15.right = node19

node19.left = node18

# Inserting new value into the BST
insert(root, 10)

# Traverse
inOrderTraversal(root) 


 
# Operation	Time	Auxiliary Space
# BST Search	O(h)	O(h)
# BST Insertion	O(h)	O(h)

# Where h = height of the BST.

# Cases

# Balanced BST:

# h = O(log n)

# So:

# Time  = O(log n)
# Space = O(log n)

# Worst-case skewed BST:

# h = O(n)

# So:

# Time  = O(n)
# Space = O(n)
# What to write in an interview

# For both:

# Time: O(h), where h is the height of the BST. 
# O(log n) for a balanced BST and O(n) in the worst case. 
# Auxiliary space: O(h) due to recursion.
