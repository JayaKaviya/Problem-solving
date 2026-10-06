# iT IS GREEDY / DYNAMIC APPROACH 

# Maximum Subarray Sum — Kadane's Algorithm ⭐⭐⭐⭐⭐
# Question

# Given an array of integers, find the contiguous subarray with the maximum sum and return both the maximum sum and the subarray.

# Example
# arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

# Maximum-sum subarray:

# [4, -1, 2, 1]

# Sum:
# 4 - 1 + 2 + 1 = 6


def maxSubarraySum(arr):
    current = arr[0]
    answer = arr[0]

    start = 0
    best_start = 0
    best_end = 0

    for i in range(1, len(arr)):
        if arr[i] > current + arr[i]:
            current = arr[i]
            start = i
        else:
            current = current + arr[i]

        if current > answer:
            answer = current
            best_start = start
            best_end = i

    return answer, arr[best_start:best_end + 1]


arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

print(maxSubarraySum(arr)) 

# Output
# (6, [4, -1, 2, 1])

# Complexity :
# Time: O(N)

# Space: O(1) extra space.

# Approach: Kadane's Algorithm — at every element, choose whether to continue the current subarray or start a new one.