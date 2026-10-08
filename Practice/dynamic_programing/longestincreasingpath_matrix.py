# LeetCode 329 — Longest Increasing Path in a Matrix
# Question

# Given an m × n matrix of integers, find the length of the longest strictly increasing path.

# From a cell, you can move only:

# Up
# Down
# Left
# Right

# You can move to a neighboring cell only when its value is greater than the current cell.

# Example
# 1  2  3
# 6  5  4
# 7  8  9

# Longest path:

# 1 → 2 → 3 → 4 → 5 → 6 → 7 → 8 → 9

# Output:

# 9 


class Solution:
    def longestIncreasingPath(self, matrix):

        rows = len(matrix)
        cols = len(matrix[0])

        dp = [[0] * cols for _ in range(rows)]

        directions = [
            (1, 0),
            (-1, 0),
            (0, 1),
            (0, -1)
        ]

        def dfs(r, c):

            if dp[r][c] != 0:
                return dp[r][c]

            dp[r][c] = 1

            for dr, dc in directions:

                nr = r + dr
                nc = c + dc

                if 0 <= nr < rows and 0 <= nc < cols:

                    if matrix[nr][nc] > matrix[r][c]:

                        dp[r][c] = max(
                            dp[r][c],
                            1 + dfs(nr, nc)
                        )

            return dp[r][c]

        answer = 0

        for r in range(rows):
            for c in range(cols):
                answer = max(answer, dfs(r, c))

        return answer 
    
# Complexity
# Time: O(R × C)
# Space: O(R × C)
# Approach

# DFS + Memoization

# dp[r][c] stores the longest increasing path starting from cell (r,c), 
# so we don't calculate the same cell repeatedly.