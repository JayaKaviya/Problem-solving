# Problem

# Given an array:

# arr = [2, 3, 5, 4]

# Create a Prefix XOR array.

# What is Prefix XOR?

# It means:

# At each position, XOR all elements from the beginning up to that position.

# arr:
# 2   3   5   4

# prefix:
# 2
# 2 ^ 3
# 2 ^ 3 ^ 5
# 2 ^ 3 ^ 5 ^ 4

# Calculate:

# 2 = 2

# 2 ^ 3 = 1

# 1 ^ 5 = 4

# 4 ^ 4 = 0

# So:

# prefix = [2, 1, 4, 0]
 
 
arr = [2, 3, 5, 4] 
n=len(arr)

prefix=[0]*(n) 

prefix[0]=arr[0] 

for i in range(1,n):
    
    prefix[i]= prefix[i-1]^arr[i]  
    
print(prefix)

# Output:

# [2, 1, 4, 0]

# Complexity
# Time  : O(n)
# Space : O(n)