# ### Question

# Given an array:

# ```text
# ARR = [7, 8, 5, 5, 9, 2, 2, 0, 1, 6]
# ```

# you can choose **any starting position** and traverse the array in either:

# * **Clockwise direction**
# * **Anti-clockwise direction**

# This produces a sequence `RES` containing all `N` elements exactly once.

# For a sequence:

# ```text
# RES = [a1, a2, a3, ..., aN]
# ```

# define:

# ```text
# value(RES) =
# a1
# + (a1 ^ a2)
# + (a1 ^ a2 ^ a3)
# + ...
# + (a1 ^ a2 ^ ... ^ aN)
# ```

# where `^` represents the **bitwise XOR** operator.

# Find the **maximum possible `value(RES)`** among all possible starting positions and both directions.

# ### Example

# If:

# ```text
# RES = [5, 8, 7, 6, 1, 0, 2, 2, 9, 5]
# ```

# then:

# ```text
# value(RES)
# = 5
# + (5 ^ 8)
# + (5 ^ 8 ^ 7)
# + ...
# + (5 ^ 8 ^ 7 ^ 6 ^ 1 ^ 0 ^ 2 ^ 2 ^ 9 ^ 5)

# = 99
# ```

# **Find the maximum possible value for the given `ARR`.**


arr = [7, 8, 5, 5, 9, 2, 2, 0, 1, 6]

n = len(arr)
max_val = 0

for start in range(n):

    # Clockwise
    res = [arr[(start + i) % n] for i in range(n)]

    ans = 0
    total = 0

    for i in res:
        ans ^= i
        total += ans

    max_val = max(max_val, total)

    # Anti-clockwise
    res = [arr[(start - i) % n] for i in range(n)]

    ans = 0
    total = 0

    for i in res:
        ans ^= i
        total += ans

    max_val = max(max_val, total)

print(max_val)