## Longest Increasing Subsequence (LIS)

### Question

# Given an array of integers, find the **length of the longest subsequence** in which the elements are in strictly increasing order.

# A **subsequence** does not need to be contiguous. We can skip elements, but their original order must be maintained.

# ### Example

# ```python
# arr = [10, 9, 2, 5, 3, 7, 101, 18]
# ```

# One longest increasing subsequence is:

# ```text
# 2 → 5 → 7 → 101
# ```

# or

# ```text
# 2 → 5 → 7 → 18
# ```

# Output - Length:

# 4


# ### Code

arr = [10, 9, 2, 5, 3, 7, 101, 18]
n = len(arr)
dp = [1] * n

for i in range(n):
    for j in range(i):
        if arr[j] < arr[i]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))


# arr:  10   9   2   5   3   7   101   18
# dp:    1   1   1   2   2   3    4     4
### Complexity

# * **Time Complexity:** `O(n²)`
#   The outer loop runs `n` times and the inner loop can also run up to `n` times.

# * **Space Complexity:** `O(n)`
#   The `dp` array stores one value for every element.

# **Important:** `dp[i]` = length of the longest increasing subsequence **ending at `arr[i]`**.
