# Single Number Using XOR ⭐⭐⭐⭐⭐
# Problem

# Given an array where every element appears exactly twice except one element, find the element that appears only once.

# Example
# arr = [4, 1, 2, 1, 2]

# Output:

# 4
# Approach

# Use XOR on every element. 


arr = [4, 1, 2, 1, 2]

ans = 0

for x in arr:
    ans ^= x

print(ans) 


# Complexity
# Time  : O(n)
# Space : O(1)