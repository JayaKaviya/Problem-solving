# Question

# Given an array of integers and a target sum, 
# determine whether any subset of the array adds up exactly to the target.
# Each element can be used at most once.

# Example
# arr = [3, 4, 5, 2]
# target = 9

# A valid subset is:
# 4 + 5 = 9

# So the output is:
# True 


arr = [3, 4, 5, 2]
target = 9

dp = [False] * (target + 1)
dp[0] = True

for x in arr:
    for s in range(target, x - 1, -1):
        dp[s] = dp[s] or dp[s - x]

print(dp[target]) 

#moving fro backward because we want to use each element at most once.
# If we move forward, we ight use the same element multiple times. 

# dp[s] means:

# Can I make sum s using the elements processed so far?

# For every number x, we have two choices:

# Don't take x → dp[s] stays as it is.
# Take x → we need to have already made s - x.

# Therefore:

# dp[s] = dp[s] or dp[s - x]

# For example, when:

# x = 5
# s = 9

# we ask:

# Can I make 9 already?
# OR
# Can I make 9 - 5 = 4?

# Since 4 can be made:

# 4 + 5 = 9

# so:

# dp[9] = True

# We traverse from right to left because each array element can be used only once.

# Complexity

# Let:

# n = number of elements
# T = target

# Time: O(nT)

# Space: O(T)