# Find the 5 Smallest Elements

# Given an array containing 10⁹ elements, find the 5 smallest elements without sorting the entire array.

# Example
# arr = [10, 3, 7, 1, 8, 2, 5]

# The 5 smallest elements are:

# [1, 2, 3, 5, 7]
# Approach: Max Heap of Size 5

# We maintain a max heap containing only 5 elements.

# Why max heap?

# Suppose our current 5 smallest are:

# [1, 3, 5, 7, 10]

# The largest among them is 10.

# If we find a new element 2, we don't need to compare it with every element.

# We simply remove the largest (10) and add 2:

# [1, 2, 3, 5, 7]

# So the heap always keeps the 5 smallest elements seen so far. 


import heapq

arr = [10, 3, 7, 1, 8, 2, 5]

heap = []

for x in arr:

    if len(heap) < 5:
        heapq.heappush(heap, -x)

    elif x < -heap[0]:
        heapq.heapreplace(heap, -x)

answer = sorted([-x for x in heap])

print(answer) 

# Output:

# [1, 2, 3, 5, 7]


# Explanation
# Step 1
# heap = []

# Create an empty heap.

# We will allow it to contain at most 5 elements.

# Step 2
# for x in arr:

# Go through every element.

# For an array of 10⁹ elements, we scan all 10⁹ elements once.

# Step 3
# if len(heap) < 5:

# If we haven't collected 5 elements yet, simply add the current element.

# heapq.heappush(heap, -x)

# Python's heapq is a min heap.

# But we need a max heap.

# So we store negative values.

# For example:

# actual values:
# 10, 3, 7

# stored:
# -10, -3, -7

# The smallest negative number corresponds to the largest actual number.

# So:

# heap[0]

# represents the largest of our 5 candidates.

# Step 4

# Once we already have 5 elements:

# elif x < -heap[0]:

# We ask:

# Is the new element smaller than the largest element currently in our 5?

# For example:

# current 5 smallest:

# [1, 3, 5, 7, 10]

# Largest = 10.

# New element:

# 2

# Since:

# 2 < 10

# 2 deserves to be in our 5 smallest.

# Step 5
# heapq.heapreplace(heap, -x)

# Remove the largest current candidate and insert the new smaller value.

# So:

# Before:

# [1, 3, 5, 7, 10]

# New value = 2

# After:

# [1, 2, 3, 5, 7]
# Step 6

# Finally:

# answer = sorted([-x for x in heap])

# The heap contains the correct 5 smallest elements, but not necessarily in sorted order.

# So we convert them back from negative values:

# [-7, -5, -3, -1, -2]

# becomes:

# [7, 5, 3, 1, 2]

# Then sorted() gives:

# [1, 2, 3, 5, 7]

# We only sort 5 elements, not the entire array.

# Complexity

# Let:

# n = number of elements
# k = 5

# For every element, heap operations cost:

# O(log k)

# So:

# Time = O(n log k)

# Since k = 5:

# O(n log 5) = O(n)

# Space:

# O(k)

# Since k = 5:

# O(1)

# Final sorted():

# O(k log k)

# Since k = 5:

# O(1)
# Final answer
# Time Complexity  : O(n)
# Space Complexity : O(1)

# explanation:

# “Since I only need the 5 smallest elements, I maintain a max heap of size 5 while scanning the array once.
# Whenever a new element is smaller than the largest element in the heap, I replace it. 
# This gives O(n log 5), which is effectively O(n), with O(5), effectively O(1), extra space.”