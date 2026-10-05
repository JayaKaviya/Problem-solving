# Maximum Sum Alternating Sign Subsequence - Its not the same what I thought
# Question

# Given an array of positive and negative integers, select a subsequence such that the signs alternate:

# + → - → + → -

# or

# - → + → - → +

# You can skip elements, but you cannot change their original order.

# Find the maximum possible sum.

# Example:

# arr = [4, 2, -3, 5, -6]

# One valid subsequence is:

# 4 → -3 → 5
# +    -    +

# Sum:

# 4 - 3 + 5 = 6

# Answer:

# 6
# Approach

# Dynamic Programming (DP)

# We maintain only two states:

# pos = maximum sum of a valid subsequence ending with a positive number

# neg = maximum sum of a valid subsequence ending with a negative number

# For every number x:

# If x is positive

# It can:

# 1. Be skipped             → old_pos
# 2. Start a new sequence   → x
# 3. Follow a negative      → old_neg + x

# So:

# pos = max(old_pos, x, old_neg + x)
# If x is negative

# It can:

# 1. Be skipped             → old_neg
# 2. Start a new sequence   → x
# 3. Follow a positive      → old_pos + x

# So:
# neg = max(old_neg, x, old_pos + x)

# Code 
# pos → last chosen element is +
# neg → last chosen element is -

def max_alternating_sum(arr):
    pos = float('-inf')
    neg = float('-inf')

    for x in arr:
        old_pos = pos
        old_neg = neg

        if x > 0:
            pos = max(old_pos, x, old_neg + x)
        else:
            neg = max(old_neg, x, old_pos + x)

    return max(pos, neg)


arr = [4, 2, -3, 5, -6]

print(max_alternating_sum(arr))
# Output
# 6


# Complexity
# Time: O(n) — process every element once.
# Space: O(1) — only pos, neg, old_pos, and old_neg.

# Pattern to remember:
# Alternating signs + subsequence + maximize sum → DP with two states (pos, neg).