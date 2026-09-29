# Question

# Find the longest subarray containing at most K zeros.

# arr = [1, 1, 0, 0, 1, 1, 1]
# k = 2

# Answer:

# 7

# because the entire array has exactly two zeros.

# Now:

# arr = [1, 1, 0, 0, 1, 0, 1]
# k = 2

# The window cannot contain more than two zeros. 

# Given:

# arr = [1, 1, 0, 0, 1, 1, 1]
# k = 2

# Count the zeros in the entire array:

# [1, 1, 0, 0, 1, 1, 1]
#        ↑  ↑
#        0  0

# There are exactly 2 zeros.

# And the condition is:

# at most 2 zeros

# "At most 2" means:

# 0 zeros  ✓
# 1 zero   ✓
# 2 zeros  ✓
# 3 zeros  ✗

# Since the entire array has only 2 zeros, the entire array is a valid subarray.

# Its length is:

# [1, 1, 0, 0, 1, 1, 1]
#  ↑                 ↑
#  1                 7

# So:

# Answer = 7

arr = [1, 1, 0, 0, 1, 0, 1]
k = 2

left = 0
zeros = 0
maximum = 0

for right in range(len(arr)):

    if arr[right] == 0:
        zeros += 1

    while zeros > k:
        if arr[left] == 0:
            zeros -= 1

        left += 1

    maximum = max(maximum, right - left + 1)

print(maximum)  

# This is essentially the same pattern as:

# Longest substring satisfying a condition.

# Only the condition changes.

# Time  : O(n)
# Space : O(1)