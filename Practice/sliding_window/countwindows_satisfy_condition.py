# Example:

# Count subarrays of size K whose sum is greater than or equal to X.

# Example
# arr = [2, 1, 5, 1, 3, 2]
# k = 3
# x = 7

# Windows:

# [2,1,5] → 8 ✓
# [1,5,1] → 7 ✓
# [5,1,3] → 9 ✓
# [1,3,2] → 6 ✗

# Answer:

# 3 


arr = [2, 1, 5, 1, 3, 2]

k = 3
x = 7

window_sum = sum(arr[:k])
count = 0

if window_sum >= x:
    count += 1

for i in range(k, len(arr)):
    window_sum += arr[i]
    window_sum -= arr[i - k]

    if window_sum >= x:
        count += 1

print(count) 

# Output:

# 3
# Complexity
# Time  : O(n)
# Space : O(1)