# Minimum Operations to Make Array Empty problem, where each operation removes exactly 2 or exactly 3 equal elements, the key idea is the remainder when frequency is divided by 3: 0, 1, or 2.

# Question

# Given an integer array, in one operation you can:

# Remove 2 equal elements, or
# Remove 3 equal elements

# Return the minimum number of operations needed to remove all elements.

# If it is impossible, return -1.

# Example
# arr = [2, 3, 3, 2, 2, 4, 2, 3, 4]

# Frequencies:

# 2 → 4
# 3 → 3
# 4 → 2

# Answer:

# 4

# Because:

# 2 → 4 elements → 2 + 2 → 2 operations
# 3 → 3 elements → 3 → 1 operation
# 4 → 2 elements → 2 → 1 operation

# Total = 2 + 1 + 1 = 4
# Approach Used
# HashMap / Frequency Counting + Greedy

# First, count how many times each number appears.

# For every frequency, we try to make as many groups of 3 as possible because:

# 3 elements → 1 operation
# 2 elements → 1 operation

# So groups of 3 are generally better.

# The important part is the remainder after dividing by 3 

from collections import Counter

def minOperations(arr):
    freq = Counter(arr)

    operations = 0

    for count in freq.values():

        if count == 1:
            return -1

        elif count % 3 == 0:
            operations += count // 3

        elif count % 3 == 1:
            operations += (count - 4) // 3 + 2

        else:
            operations += count // 3 + 1

    return operations


arr = [2, 3, 3, 2, 2, 4, 2, 3, 4]

print(minOperations(arr)) 

# Output:
# 4 

# The main pattern
# count % 3 == 0 → all groups of 3

# count % 3 == 2 → groups of 3 + one group of 2

# count % 3 == 1 → replace one group of 3 + 1
#                   with two groups of 2

# So this is a frequency counting + greedy remainder problem.

# Complexity
# Let n = number of elements.

# Time: O(n)
# Space: O(n)