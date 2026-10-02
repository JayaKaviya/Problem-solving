# 0/1 Knapsack ⭐⭐⭐⭐⭐
# Question

# You are given n items. Each item has a weight and a value. You have a bag with a fixed capacity.

# Find the maximum total value you can put in the bag.

# Each item can be taken at most once.

# Example
# weights = [1, 3, 4, 5]
# values  = [1, 4, 5, 7]
# capacity = 7

# Output:

# 9

# Because we can take:

# Item 2 → weight = 3, value = 4
# Item 3 → weight = 4, value = 5

# Total weight = 3 + 4 = 7
# Total value  = 4 + 5 = 9
# Logic

# For every item, we have 2 choices:

# 1. Don't take the item
# 2. Take the item

# If we don't take it:

# dp[i-1][w]

# If we take it:

# value + dp[i-1][w-weight]

# Here:

# i - 1 → use previous items, so the current item isn't reused
# w - weight → remaining capacity after taking the current item

# Therefore:

# dp[i][w] = max(
#     dp[i-1][w],
#     value + dp[i-1][w-weight]
# ) 


weights = [1, 3, 4, 5]
values = [1, 4, 5, 7]
capacity = 7

n = len(weights)

dp = [[0] * (capacity + 1) for i in range(n + 1)]

for i in range(1, n + 1):
    weight = weights[i - 1]
    value = values[i - 1]

    for w in range(capacity + 1):
        # Don't take the item (so taking previous items with the same capacity)
        dp[i][w] = dp[i - 1][w]
        
        #Take the item (if it fits in the bag)
        if weight <= w: 
            #finding the maximum value of that item or value + previous items with the remaining capacity
            dp[i][w] = max(dp[i][w], value + dp[i - 1][w - weight])

print(dp[n][capacity]) 


# Complexity
# Time: O(n × W)
# Space: O(n × W)

# Where:

# n = number of items
# W = bag capacity

# Pattern to remember:
# 0/1 Knapsack = TAKE or DON'T TAKE → choose MAX.