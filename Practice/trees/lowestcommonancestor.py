# Lowest Common Ancestor (LCA) ⭐⭐⭐⭐
# Question

# Given two nodes p and q, find their Lowest Common Ancestor (LCA) — the deepest node that is an ancestor of both.

# Example:

#         1
#        / \
#       2   3
#      / \
#     4   5

# For:

# p = 4
# q = 5

# Both 4 and 5 have 2 as their common ancestor.

#         1
#        /
#       2  ← LCA
#      / \
#     4   5

# Answer: 2

# Logic

# At each node:

# If root is None → return None.
# If root is p or q → return root.
# Search the left subtree.
# Search the right subtree.
# If both sides find a node, current root is the LCA.
# Otherwise, return whichever side found a node. 


def lca(root, p, q):

    if root is None or root.val == p or root.val == q:
        return root

    left = lca(root.left, p, q)
    right = lca(root.right, p, q)

    if left and right:
        return root

    return left or right


print(lca(root, 4, 5).val) 


# Output:

# 2
# Why left and right?

# For nodes 4 and 5:

#         2
#        / \
#       4   5

# At node 2:

# left  = 4
# right = 5

# Both sides found a target:

# if left and right:
#     return root

# So root is 2.

# 4 → 2 ← 5
#     ↑
#    LCA
# Why left or right?

# If only one side finds a target:

# left  = 4
# right = None

# then:

# return left or right

# returns 4.

# This doesn't mean 4 is the final LCA. It simply tells the parent:

# “I found one of the target nodes in my subtree.”

# Complexity
# Time: O(n) — each node may be visited once.
# Auxiliary space: O(h) — recursion stack.
# Worst-case space: O(n) for a completely skewed tree. 