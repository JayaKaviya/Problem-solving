# Count Subarrays With At Most K Distinct Elements ⭐⭐⭐⭐

# This is a more advanced and useful variation.

# Example
# arr = [1, 2, 1]
# k = 2

# Every subarray has at most 2 distinct values:

# [1]
# [2]
# [1]

# [1,2]
# [2,1]

# [1,2,1]

# Total:

# 6 

arr = [1, 2, 1]
k = 2

freq = {}

left = 0
count = 0

for right in range(len(arr)):

    x = arr[right]
    freq[x] = freq.get(x, 0) + 1

    while len(freq) > k:
        x = arr[left]

        freq[x] -= 1

        if freq[x] == 0:
            del freq[x]

        left += 1

    count += right - left + 1

print(count) 

# Complexity	Answer
# Time	O(n) average
# Space	O(k), worst-case O(n)