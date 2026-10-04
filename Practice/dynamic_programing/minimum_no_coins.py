# Minimum Number of Coins — DP
# Question

# Given a list of coin denominations and an amount, find the minimum number of coins needed to make that amount.

# Each coin can be used any number of times.

# If the amount cannot be made, return -1.

# Example
# coins = [1, 3, 4]
# amount = 6

# Minimum coins:
# 3 + 3 = 6

# Answer:

# 2
# Approach

# Use 1D Dynamic Programming. 


coins = [1, 3, 4]
amount = 6

dp = [float('inf')] * (amount + 1)
dp[0] = 0

for i in range(1, amount + 1):
    for coin in coins:
        if coin <= i:
            dp[i] = min(dp[i], dp[i - coin] + 1)
            
if dp[amount] == float('inf'):
    print(-1)
else:
    print(dp[amount]) 
    
# Time Complexity: O(A × N)

# Why?

# Outer loop runs A times.
# Inner loop checks all N coins.
# So:
# A × N

# Therefore:

# Time = O(A × N)

# Space Complexity: O(A)