# # Maximum Sum with Alternating + and - 


# Question

# Given an array of positive integers, choose a subsequence such that the selected elements get alternating signs:

# +  -  +  -  + ...

# Find the maximum possible sum.

# Example
# arr = [1, 2, 3, 4, 1, 2]

# One possible subsequence:
# 4, 1, 2

# Give alternating signs:
# +4 -1 +2 = 5

# So the answer is:
# 5 

def findMax(arr):
    n = len(arr)

    dp = [[0, 0] for _ in range(n)]

    dp[n - 1][0] = arr[n - 1]
    dp[n - 1][1] = 0

    for i in range(n - 2, -1, -1):
        # If we need +, we can either skip the current number, take it as + and choose the next number as -
        dp[i][0] = max( dp[i + 1][0],arr[i] + dp[i + 1][1])
         
        #If we need -, we can either skip the current number, take it as - and choose the next number as +
        dp[i][1] = max(dp[i + 1][1],-arr[i] + dp[i + 1][0])

    return dp[0][0]  


arr = [1, 2, 3, 4, 1, 2]

print(findMax(arr))

# Logic

# There are only 2 states.

# [0] = next selected number needs +
# [1] = next selected number needs -
# State [0]
# dp[i][0] = max(dp[i+1][0], arr[i] + dp[i+1][1])

# We need +.

# Skip:

# dp[i+1][0]

# We didn't use the number, so we still need +.

# [0] → SKIP → [0]

# Take:

# arr[i] + dp[i+1][1]

# We use the number as +.

# Now we need -.

# [0] → TAKE → [1]
# State [1]
# dp[i][1] = max(dp[i+1][1], -arr[i] + dp[i+1][0])

# We need -.

# Skip:

# dp[i+1][1]

# We didn't use the number, so we still need -.

# [1] → SKIP → [1]

# Take:

# -arr[i] + dp[i+1][0]

# We use the number as -.

# Now we need +.

# [1] → TAKE → [0]
# The whole logic
#              SKIP       TAKE
             
# [0] need +   [0]        +arr[i] → [1]

# [1] need -   [1]        -arr[i] → [0]

# That's the main thing to remember:

# Skip → state stays the same.
# Take → sign changes → state changes.

# Why start from the end?

# We calculate the answer for the last element first:

# dp[n-1][0] = arr[n-1]
# dp[n-1][1] = 0

# For the last element:

# Need + → taking it gives +arr[n-1], so best is arr[n-1].
# Need - → taking a positive number would make the sum smaller, so we can simply skip it and get 0.

# Then we move:

# last → second last → ... → first

# Finally:

# return dp[0][0]

# At the beginning, we are at index 0, and the first selected element gets +, so we start in state [0].

# Complexity

# Time: O(N)

# Each element is processed once.

# Space: O(N)

# We store 2 states for every element:

# N × 2
# DP type

# Bottom-up, state-based DP with Skip/Take choices.