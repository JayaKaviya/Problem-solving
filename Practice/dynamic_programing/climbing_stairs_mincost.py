# 1. Min Cost Climbing Stairs , (2nd approach down)
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
    dp[i] = min(  dp[i - 1] + cost[i - 1], dp[i - 2] + cost[i - 2])
 
print(dp[n]) 



# Climbing Stairs - 2nd Question (similar to Fibonacci series)
# Question

# You are at the bottom.

# You can move:

# 1 step
# 2 steps

# Question:

# How many different ways can you reach step n?

# Example:

# n = 4

# Ways:

# 1 + 1 + 1 + 1
# 1 + 1 + 2
# 1 + 2 + 1
# 2 + 1 + 1
# 2 + 2

# So:

# Answer = 5

# Code
n = 4

a = 1
b = 1

for i in range(2, n + 1):
    c = a + b
    a = b
    b = c

print(b)

# Output:

# # 5
# What are a and b?

# They simply store the previous two answers.

# a = previous answer
# b = current answer

# We don't need the entire dp array.

# Complexity
# Time  = O(n)
# Space = O(1) 


# Step 2: Start with small answers
# step 0 → 1 way
# step 1 → 1 way
# step 2 → 2 ways
# step 3 → 3 ways
# step 4 → 5 ways

# Why step 2?

# 1 + 1
# 2

# So there are 2 ways.

# Then:

# step 3 = step 2 + step 1
#        = 2 + 1
#        = 3

# Then:

# step 4 = step 3 + step 2
#        = 3 + 2
#        = 5