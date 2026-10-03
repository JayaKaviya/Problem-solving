# Maximum Depth of a Binary Tree ⭐⭐⭐⭐⭐

# Question: Find the maximum number of nodes along a path from the root to a leaf.

# For our example, the longest path is:
    #     1
    #    / \
    #   2   3
    #  / \
    # 4   5
# 1 → 2 → 4

# Answer: 3 nodes.

# How to choose the logic

# The depth of a node is: ( why 1 ? add the current node to the depth of its children )
# 1 + maximum depth of its children

# So:

# depth = 1 + max(left depth, right depth)
# Code
def max_depth(root):
    if root is None:
        return 0

    left = max_depth(root.left)
    right = max_depth(root.right)

    return 1 + max(left, right)

# Call it using:

print(max_depth(root))

# Output: 3

# Code explanation

# If the node is None, depth is 0.

# Calculate the left subtree's depth.

# Calculate the right subtree's depth.

# Return the larger depth plus 1 for the current node.

# Time: O(n)

# Auxiliary space: O(h) for recursion; worst case O(n).

# Recognition clue: If the question asks for the height or maximum depth, think recursive left/right depth.