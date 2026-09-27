### Coding Question — Get Maximum in Generated Array

# You are given an integer `n`.

# Create an array `nums` of size `n + 1` using the following rules:

# 1. `nums[0] = 0`
# 2. `nums[1] = 1`
# 3. For every integer `i`:

#    * If `2 * i <= n`:

#      ```text
#      nums[2 * i] = nums[i]
#      ```
#    * If `2 * i + 1 <= n`:

#      ```text
#      nums[2 * i + 1] = nums[i] + nums[i + 1]
#      ```

# Return the **maximum integer** present in the array `nums`.

# ### Example 1

# **Input:**

# ```text
# n = 7
# ```

# Generated array:

# ```text
# [0, 1, 1, 2, 1, 3, 2, 3]
# ```

# **Output:**

# ```text
# 3
# ```

# ### Example 2

# **Input:**

# ```text
# n = 2
# ```

# Generated array:

# ```text
# [0, 1, 1]
# ```

# **Output:**

# ```text
# 1
# ```

# ### Constraints

# ```text
# 0 <= n <= 100
# ```
def getMaximumGenerated(n):
    if n == 0:
        return 0

    nums = [0] * (n + 1)

    nums[0] = 0
    nums[1] = 1

    for i in range(1, n + 1):
        if 2 * i <= n:
            nums[2 * i] = nums[i]

        if 2 * i + 1 <= n:
            nums[2 * i + 1] = nums[i] + nums[i + 1]

    return max(nums)