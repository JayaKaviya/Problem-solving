# Longest Common Subsequence (LCS) ⭐⭐⭐⭐⭐
# Question

# Find the length of the longest sequence of characters common to two strings, preserving their order but not necessarily their adjacency.

# s1 = "abcde"
# s2 = "ace"

# Output: 3

# The common subsequence is "ace".

# Logic: 2D DP

# Let dp[i][j] represent the LCS length for the first i characters of s1 and the first j characters of s2.

# If the current characters match:

# dp[i][j]=1+dp[i−1][j−1]

# If they do not match:

# dp[i][j]=max(dp[i−1][j],dp[i][j−1]) 


# s1 = "abcde"    → length 5
# s2 = "ace"      → length 3

# So the table is:

# 6 rows × 4 columns

# Why the extra row and column?

# Because we also need to represent an empty string.

# "" vs "ace"
# "abcde" vs ""

# If one string is empty, the LCS length is 0.

# So initially:

#       ""  a  c  e
# ""     0  0  0  0
# a      0
# b      0
# c      0
# d      0
# e      0 


s1 = "abcde"
s2 = "ace"

m = len(s1)
n = len(s2)

dp = [[0] * (n + 1) for i in range(m + 1)]

for i in range(1, m + 1):
    for j in range(1, n + 1):
        if s1[i - 1] == s2[j - 1]:
            dp[i][j] = 1 + dp[i - 1][j - 1]
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

print(dp[m][n]) 

# LCS

# Time  → O(mn)
# Space → O(mn)