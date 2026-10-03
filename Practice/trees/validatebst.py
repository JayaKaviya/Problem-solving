# Validate a BST ⭐⭐⭐⭐⭐
# Question

# Given a binary tree, check whether it is a valid Binary Search Tree (BST).

# A valid BST follows:

# left subtree  <  current node  <  right subtree

# Example of a valid BST:

#         10
#        /  \
#       5    15
#      / \     \
#     2   7     20
# How to choose the logic

# Don't check only the immediate children.

# Instead, carry a valid range (low, high) for every node.

# Left child  → upper limit becomes current node
# Right child → lower limit becomes current node

# For example, for node 7:

# 5 < 7 < 10

# So 7 is valid. 


def is_valid_bst(root):

    def check(node, low, high):

        if node is None:
            return True

        if not (low < node.val < high):
            return False

        return (
            check(node.left, low, node.val)
            and check(node.right, node.val, high)
        )

    return check(root, float('-inf'), float('inf'))


print(is_valid_bst(root)) 


# For the valid tree above:

# True
# Simple flow

# Start:

# check(10, -∞, +∞)

# For left 5:

# check(5, -∞, 10)

# For right 15:

# check(15, 10, +∞)

# Then the ranges become narrower as we go down:

#         10
#        /  \
# (-∞,10)  (10,+∞)
#     5        15

# For 7:

# check(7, 5, 10)

# So:

# 5 < 7 < 10

# Valid ✅

# Important example

# This tree is NOT a valid BST:

#         10
#        /  \
#       5    15
#           /
#          7

# Someone might incorrectly say 7 < 15, so it is okay.

# But 7 is in the right subtree of 10, so it must be greater than 10.

# Its range is:

# 10 < 7 < 15

# False ❌

# Therefore the whole tree is invalid.

# Complexity
# Time: O(n) — each node is checked once.
# Auxiliary space: O(h) — recursion stack.
# Balanced tree: O(log n) space.
# Skewed tree: O(n) space.