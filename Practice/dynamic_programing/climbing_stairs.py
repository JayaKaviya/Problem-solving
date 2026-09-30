# Min Cost Climbing Stairs
# Question

# You are given an array cost, where cost[i] is the cost of stepping on stair i.

# You can start from stair 0 or stair 1.

# From each stair, you can climb either 1 step or 2 steps.

# Find the minimum cost required to reach the top.

# Example
# cost = [10, 15, 20]

# Possible paths:

# 10 → 15 → TOP
# Cost = 10 + 15 = 25

# 10 → 20 → TOP
# Cost = 10 + 20 = 30

# 15 → TOP
# Cost = 15

# Therefore:

# Answer = 15
# Approach: Dynamic Programming

# We use a dp array.

# Meaning of dp[i]

# dp[i] = minimum cost needed to reach position i. 

# We can reach position i in two ways:

# From i-1 → move 1 step
# From i-2 → move 2 steps 

# Time Complexity
# O(n)

# We visit each position once.

# Space Complexity
# O(n)

# Because we store the dp array of size n + 1. 


# very easy

cost = [10, 15, 20]

n = len(cost)

dp = [0] * (n + 1)

dp[0] = 0
dp[1] = 0

for i in range(2, n + 1):
    dp[i] = min(
        dp[i - 1] + cost[i - 1],
        dp[i - 2] + cost[i - 2]
    )

print(dp[n])