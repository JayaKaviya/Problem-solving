# XOR Left & Right Comparison
# Problem

# Given an array, count the elements for which:

# XOR of all elements on the left < current element
# AND
# XOR of all elements on the right < current element

# Example:

# arr = [7, 8, 5, 5, 9]

# For 7:

# Left  = 0
# Right = 8 ^ 5 ^ 5 ^ 9 = 1

# Both are smaller than 7:

# 0 < 7 ✓
# 1 < 7 ✓

# So 7 is counted.

# Output:

# 1 


arr = [7, 8, 5, 5, 9]

total = 0

for x in arr:
    total ^= x

left = 0
count = 0

for i in range(len(arr)):

    right = total ^ left ^ arr[i]

    if left < arr[i] and right < arr[i]:
        count += 1

    left ^= arr[i]

print(count) 

# Complexity
# Time  : O(n)
# Space : O(1)

# Why O(n)?

# First loop → O(n)
# Second loop → O(n)
# No nested loop
# XOR operations → O(1)

# Therefore:

# O(n) + O(n) = O(n)