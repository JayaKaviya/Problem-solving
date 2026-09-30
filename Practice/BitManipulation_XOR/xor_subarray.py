# XOR of a Subarray
# Problem

# Given an array and two indices L and R, find the XOR of all elements from index L to index R.

# Example:

# arr = [2, 3, 5, 4, 7]

# L = 1
# R = 3

# We need:

# arr[1] ^ arr[2] ^ arr[3]

# = 3 ^ 5 ^ 4

# = 2 

arr = [2, 3, 5, 4, 7]

prefix = [0] * len(arr)

prefix[0] = arr[0]

for i in range(1, len(arr)):
    prefix[i] = prefix[i - 1] ^ arr[i]

L = 1
R = 3

if L == 0:
    answer = prefix[R]
else:
    answer = prefix[R] ^ prefix[L - 1]

print(answer) 


# Output
# 2


# Complexity
# Building prefix:
# O(n)

# Each XOR subarray query:
# O(1)

# Space:

# O(n)

# So:

# Time  : O(n) preprocessing + O(1) per query
# Space : O(n)
# ⭐ Formula to remember

# For this prefix array that starts with arr[0]:

# XOR(L to R) = prefix[R] ^ prefix[L - 1]

# And if L = 0:

# XOR(0 to R) = prefix[R]