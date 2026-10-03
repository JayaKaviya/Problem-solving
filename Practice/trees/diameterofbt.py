# Diameter of a Binary Tree ⭐⭐⭐⭐⭐
# Question

# Find the longest path between any two nodes in a binary tree.

# Example:

#         1
#        / \
#       2   3
#      / \
#     4   5

# Longest path:

# 4 → 2 → 1 → 3

# Number of edges:

# 4 → 2   = 1
# 2 → 1   = 1
# 1 → 3   = 1

# Total = 3

# Answer = 3

# How to choose the logic

# When you see:

# “Longest path between any two nodes”

# think Diameter.

# At every node:

# path through this node
# = left height + right height

# But we also need to return the height to the parent.

# So there are two jobs:

# ans    → stores the biggest diameter found
# return → gives the current height to the parent 


def diameter(root):
    ans = 0

    def height(node):
        nonlocal ans

        if node is None:
            return 0

        left = height(node.left)
        right = height(node.right)

        ans = max(ans, left + right)

        return 1 + max(left, right)

    height(root)

    return ans


print(diameter(root)) 

# Output:

# 3

# Complexity
# Time: O(n) — every node is visited once.
# Auxiliary space: O(h) — recursion stack, where h is tree height.
# Worst case: O(n) for a completely skewed tree.
# Remember this
# Diameter = longest path
#           ↓
# Check every node
#           ↓
# left height + right height
#           ↓
# store biggest value in ans

# return height → needed by the parent

# Important: Some questions define diameter as number of nodes instead of edges. Your example defines it as edges, so the answer is 3.