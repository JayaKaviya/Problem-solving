# Edit Distance — Simple Explanation
# 1. Question

# Given two strings word1 and word2, find the minimum number of operations needed to convert word1 into word2.

# We can perform 3 operations:

# Insert a character
# Delete a character
# Replace a character
# Example
# word1 = "horse"
# word2 = "ros"

# One possible conversion:

# horse
#  ↓ replace h → r
# rorse
#  ↓ delete r
# rose
#  ↓ delete e
# ros

# Answer:

# 3 

def minDistance(self, word1: str, word2: str) -> int:
        m = len(word1)
        n = len(word2)

        dp = [[0] * (n + 1) for _ in range(m + 1)]

        # Empty word2
        for i in range(m + 1):
            dp[i][0] = i

        # Empty word1
        for j in range(n + 1):
            dp[0][j] = j

        for i in range(1, m + 1):
            for j in range(1, n + 1):

                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]

                else:
                    dp[i][j] = min(
                        dp[i - 1][j],      # Delete
                        dp[i][j - 1],      # Insert
                        dp[i - 1][j - 1]   # Replace
                    ) + 1

        return dp[m][n]


word1 = "horse"
word2 = "ros"

print(minDistance(word1, word2)) 


# Complexity

# Let:

# m = len(word1)
# n = len(word2)

# We create an (m+1) × (n+1) table.

# We visit every cell once.

# Time
# O(m × n)
# Space
# O(m × n) 


# Approach

# We use Dynamic Programming (DP).

# Why DP?

# Because we can break the big problem into smaller string problems and save their answers.

# We create:

# dp[i][j]

# It means:

# Minimum operations needed to convert the first i characters of word1 into the first j characters of word2.

# For example:

# dp[2][3]

# means:

# Convert the first 2 characters of word1 into the first 3 characters of word2.

# 3. Logic

# There are two main cases.

# Case 1: Characters are the same

# Example:

# word1: c a
# word2: c a
#         ↑

# If the current characters are the same, we don't need any operation.

# So:

# dp[i][j] = dp[i-1][j-1]

# We simply use the previous smaller problem.

# Case 2: Characters are different

# Suppose:

# word1: c a t
# word2: c a r
#           ↑

# We have:

# t != r

# We have 3 choices.

# Delete

# Delete t:

# cat → ca

# We removed one character from word1.

# dp[i-1][j] + 1
# Insert

# Insert r:

# cat → car

# We handled one character from word2.

# dp[i][j-1] + 1
# Replace

# Replace t with r:

# cat
#  ↓
# car

# We handled one character from both strings.

# dp[i-1][j-1] + 1
# Choose the minimum

# We don't know which operation is best.

# So we try all three:

# min(
#     dp[i-1][j],      # delete
#     dp[i][j-1],      # insert
#     dp[i-1][j-1]     # replace
# ) + 1

# The +1 means:

# We just performed one operation.