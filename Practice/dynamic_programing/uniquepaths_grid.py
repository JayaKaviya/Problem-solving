# Grid DP — Unique Paths
# Question

# You are given an m × n grid. You start at the top-left cell and need to reach the bottom-right cell.

# You can move only:

# Right →
# Down ↓

# Find the number of different paths from the start to the destination.

# Example

# For a 3 × 3 grid:

# S  →  →
# ↓  ↓  ↓
# ↓  →  E

# There are 6 different paths. 


m = 3
n = 3

dp = [[1] * n for i in range(m)]

for i in range(1, m):
    for j in range(1, n):
        dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

print(dp[m - 1][n - 1]) 


# Output
# 6
# Logic

# For every cell:

# dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

# Because the current cell can be reached from:

# TOP  → current   (moving DOWN)
# LEFT → current   (moving RIGHT)

# So:

# ways to current
# =
# ways from TOP
# +
# ways from LEFT

# The DP table becomes:

# 1  1  1
# 1  2  3
# 1  3  6
# Complexity
# Time: O(m × n)
# Space: O(m × n)

# Because we calculate every cell of the m × n DP table once.