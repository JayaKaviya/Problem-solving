# Maximum Length of a Window Under a Given Condition
# Question

# Given an array of positive integers and an integer k,
# find the maximum length of a contiguous subarray whose sum is less than or equal to k.

# Example
# arr = [2, 1, 5, 1, 3, 2]
# k = 7

# The longest valid window is:
# [1, 3, 2]

# Sum:
# 1 + 3 + 2 = 6

# Length:
# 3
# Answer = 3 

arr = [2, 1, 5, 1, 3, 2]
k = 7
def maxLength(arr, k):
    left = 0
    total = 0
    answer = 0

    for right in range(len(arr)):
        total += arr[right]

        while total > k:
            total -= arr[left]
            left += 1

        answer = max(answer, right - left + 1)

    return answer 


# Complexity
# Time: O(N)

# Each element is added by right once and removed by left at most once.
# Space: O(1)

# Only a few variables are used.