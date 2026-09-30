# 1.Maximum XOR of Two Elements ⭐⭐⭐⭐
# Question
# Given an array, find the maximum XOR value of any two elements.
# Example:
# arr = [3, 10, 5, 25, 2, 8]
# Find:
# max(arr[i] ^ arr[j])
# Answer: 28
# Because: 5 ^ 25 = 28 


arr = [3, 10, 5, 25, 2, 8]
maximum = 0
for i in range(len(arr)):
    for j in range(i + 1, len(arr)):
        maximum = max(maximum, arr[i] ^ arr[j])
print(maximum) 


# Output:

# 28
# Complexity
# Time  : O(n²)
# Space : O(1)

# Because we check every pair of elements.
# Optimized Approach
# Use a Binary Trie to find the maximum XOR in:
# Time  : O(n × B)
# Space : O(n × B)
# where B is the number of bits (usually 32). 


# 2.XOR Subset ⭐⭐⭐⭐

# This one can have several versions.
# Since you previously encountered the Maximum XOR Subset problem,
# this is the important version for you.

# Problem

# Given an array, choose at most K elements and maximize their XOR.

# arr = [1, 2, 4, 7]
# k = 2

# maximum = 0

# for i in range(len(arr)):
#     for j in range(i + 1, len(arr)):
#         maximum = max(maximum, arr[i] ^ arr[j])

# for x in arr:
#     maximum = max(maximum, x)

# print(maximum) 

# Output:

# 7

# Complexity:

# Time  = O(N²)
# Space = O(1)