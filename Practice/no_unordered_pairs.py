# Given an array, find the number of unordered pairs (i, j) such that:

# i < j
# arr[i] + arr[j] = 0
# j % 2 != 0 — the second index j must be odd.

# Because the pairs are unordered, (i, j) and (j, i) are considered the same pair. 
# Using i < j ensures we count each pair only once.

# Example
# arr = [-2, 5, 2, -5, 5]
# index =  0  1  2   3  4

# Valid pair:

# (1, 3)

# arr[1] + arr[3]
# = 5 + (-5)
# = 0

# j = 3 is odd, so it is counted.

# Approach Used: HashMap + Complement

# For every j, we need:

# arr[i] + arr[j] = 0

# Therefore:

# arr[i] = -arr[j]

# So for every j, check whether -arr[j] has already appeared before.

# We use a HashMap to store the frequency of previous elements.

# The condition:

# j % 2 != 0

# ensures that we count only when j is odd. 


arr = [-2, 5, 2, -5, 5]

freq = {}
count = 0

for j in range(len(arr)):

    if j % 2 != 0:

        required = -arr[j]

        if required in freq:
            count += freq[required]

    freq[arr[j]] = freq.get(arr[j], 0) + 1

print(count) 

# Complexity
# Time: O(n) average
# Space: O(n)
# Pattern to remember
# Pair + target sum + need previous matching value
#                 ↓
#              HashMap