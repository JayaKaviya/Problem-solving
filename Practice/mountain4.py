# ### Coding Question — Minimum Changes to Make a Mountain

# You are given an array of `N` integers.

# You need to change the array into a **mountain**.

# An array is called a mountain if:

# * The elements increase by exactly `1` as we move from either end toward the middle.
# * The elements decrease by exactly `1` after reaching the middle.
# * Elements at equal distances from the two ends must be equal.
# * The values can be **zero or negative**.

# For example:

# ```text
# [1, 2, 3, 2, 1]       → Mountain
# [6, 7, 8, 8, 7, 6]    → Mountain
# ```

# These are **not** mountains:

# ```text
# [1, 2, 4, 2, 1]
# ```

# because `2 → 4` increases by `2`.

# ```text
# [1, 2, 3, 1]
# ```

# because the elements are not symmetric.

# ### Task

# Find the **minimum number of elements that must be changed** to make the array a mountain.

# ### Input

# ```text
# N
# A[0]
# A[1]
# ...
# A[N-1]
# ```

# ### Constraints

# ```text
# 1 ≤ N ≤ 100000
# 1 ≤ A[i] ≤ 1000000
# ```

# ### Example 1

# **Input:**

# ```text
# 5
# 1
# 2
# 3
# 4
# 5
# ```

# **Output:**

# ```text
# 2
# ```

# Because we can change the array to:

# ```text
# [1, 2, 3, 2, 1]
# ```

# which requires changing `4` and `5`. 


N = 5
A =[1,2,3,4,5]

count = {}
maximum = 0

for i in range(N):
    distance = min(i, N - 1 - i)

    value = A[i] - distance

    if value not in count:
        count[value] = 0

    count[value] += 1

    maximum = max(maximum, count[value])

answer = N - maximum

print(answer)
