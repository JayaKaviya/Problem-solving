# Partition Equal Subset Sum
# Question

# Given an array of positive integers, determine whether the array can be divided into two subsets with equal sum.

# Example:

# arr = [1, 5, 11, 5]

# Output: True

# Because we can divide it as:

# [11]       → 11
# [1, 5, 5]  → 11 

#if the total sum is odd, we cannot divide it into two equal subsets. 
# If the total sum is even, we can check if there is a subset with sum equal to total // 2.

arr = [1, 5, 11, 5]
total = sum(arr)
if total % 2 != 0:
    print(False)
else:
    target = total // 2

    dp = [False] * (target + 1)
    dp[0] = True

    for x in arr:
        for s in range(target, x - 1, -1):
            dp[s] = dp[s] or dp[s - x]

    print(dp[target]) 
    
#     Complexity
# Time: O(n × T)
# Space: O(T)

# Where:

# n = number of elements
# T = total // 2

# Pattern: This is basically Subset Sum DP.