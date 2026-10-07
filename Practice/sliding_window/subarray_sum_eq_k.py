# 1.Given an array of integers arr and an integer k, 
# find the number of continuous subarrays whose sum is equal to k.
# ------------ IT WORKS FOR BOTH POSITIVE AND NEGATIVE INTEGERS ---------------
# Example:

# arr = [1, 2, 3, 4, 2]
# k = 5
# Subarrays whose sum is 5
# [1, 2, 3] → 6 ❌
# [1, 2]     → 3 ❌
# [2, 3]     → 5 ✅
# [1, 2, 3, 4] → 10 ❌
# [3, 2]     → 5 ❌
# [1, 4]     → 5 ❌

# Actually, let's identify them systematically:

# [1, 2, 3, 4, 2]

# Valid subarrays are:

# [2, 3]   → 5
# [1, 2]   → 3
# [1, 2, 3] → 6
# [4, 2]   → 6
# [3, 4]   → 7
# [1, 4]   → 5

# So the answer is:

# 2

# The two valid subarrays are:

# [2, 3]
# [1, 4]

def subarraySum(arr, k):
    prefix = 0
    count = 0
    freq = {0: 1}

    for num in arr:
        prefix += num

        if prefix - k in freq:
            count += freq[prefix - k]

        freq[prefix] = freq.get(prefix, 0) + 1

    return count


arr = [1, 2, 3, 4, 2]
k = 5

print(subarraySum(arr, k))  

# Complexity
# Time:  O(n)
# Space: O(n) 


#2. Question - POSITIVE INTEGERS ONLY

# Given an array containing only positive integers and an integer k, 
# find the number of continuous subarrays whose sum is equal to k.

# Example:

# arr = [1, 2, 3, 4, 2]
# k = 5

# Answer:

# 2

# The subarrays are:

# [2, 3] → 5
# [1, 4] → 5
# Solution
def subarraySum(arr, k):
    left = 0
    current = 0
    count = 0

    for right in range(len(arr)):
        current += arr[right]

        while current > k:
            current -= arr[left]
            left += 1

        if current == k:
            count += 1

    return count


arr = [1, 2, 3, 4, 2]
k = 5

print(subarraySum(arr, k)) 

# Complexity
# Time:  O(n)
# Space: O(1)

# For positive numbers → sliding window is the easiest solution.

# For positive + negative numbers → prefix sum + hashmap. 


# 3.Yes. For **positive numbers only**, your code is finding the **actual subarrays**
# ## Question

# **Given an array of positive integers and an integer `k`, find all continuous subarrays whose sum is equal to `k`.**

# Example:

# ```python
# arr = [1, 2, 3, 4, 2]
# k = 5
# ```

# Expected answer:

# ```text
# [([2, 3], 5), ([1, 4], 5)]
# ```

# ## Your solution

# There is one important fix: use **`while` instead of `if`**.

# ```python
def subarraySumK(arr, k):
    left = 0
    current = 0
    result = []

    for right in range(len(arr)):

        current += arr[right]

        while current > k:
            current -= arr[left]
            left += 1

        if current == k:
            result.append((arr[left:right + 1], current))

    return result


arr = [1, 2, 3, 4, 2]
k = 5

print(subarraySumK(arr, k))
# ```

# ### Output

# ```text
# [([2, 3], 5), ([1, 4], 5)]
# ```

# ### Why `while`?

# Suppose:

# ```text
# arr = [1, 2, 3]
# k = 3
# ```

# After adding `3`:

# ```text
# current = 1 + 2 + 3
#         = 6
# ```

# We need to keep removing from the left:

# ```text
# 6 > 3
# remove 1
# current = 5

# 5 > 3
# remove 2
# current = 3
# ```

# Now we found:

# ```text
# [3]
# ```

# If you use `if`, you remove only **one** element:

# ```text
# 6 → 5
# ```

# and stop, even though `5 > 3`.

# So:

# ```python
# while current > k:
# ```

# is necessary.

# ### Complexity

# ```text
# Time:  O(n)
# Space: O(n)
# ```

# `O(n)` space here is because `result` stores the actual subarrays.

# If you only **count** them instead of storing them:

# ```text
# Space: O(1)
# ```

# And remember:

# > **Positive numbers → sliding window works.**
# > **Positive + negative numbers → use prefix sum + hashmap.**
