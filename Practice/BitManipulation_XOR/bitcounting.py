# Absolutely. For **Bit Counting**, keep these two approaches separately.

# # Problem

# > Given an integer `n`, count the number of `1` bits in its binary representation.

# Example:

# ```text
# n = 13

# 13 → 1101
# ```

# There are **3 ones**, so answer = `3`.

# ---

# # Approach 1 — `% 2` and `// 2`

### Code


n = 13
count = 0

while n > 0:
    count += n % 2
    n //= 2

print(count)




### Complexity

# ```text
# Time  : O(log n)
# Space : O(1)
# ```

# Why `O(log n)`?

# Because we keep dividing by `2`:

# ```text
# 13 → 6 → 3 → 1 → 0
# ```

# The number of divisions needed is approximately `log₂(n)`.

# ---

# Approach 2 — `n & (n - 1)` ⭐

### Code


n = 13
count = 0

while n:
    n = n & (n - 1)
    count += 1

print(count)


### Complexity

# Time  : O(k)
# Space : O(1)


# Since the maximum number of `1` bits is at most the number of binary digits:

# ```text
# k ≤ log₂(n)
# ```

# Worst case:

# ```text
# Time  : O(log n)
# Space : O(1)
# ```



## ⭐ Interview comparison

# | Approach               | Idea                       |     Time | Space |
# | ---------------------- | -------------------------- | -------: | ----: |
# | `% 2`, `// 2`          | Check each binary bit      | O(log n) |  O(1) |
# | `n & (n-1)`            | Remove each `1` bit        |     O(k) |  O(1) |
# | `n & (n-1)` worst case | If almost/all bits are `1` | O(log n) |  O(1) |

# ### What to remember

# ```text
# n % 2       → gets the last bit
# n // 2      → removes the last bit
# ```

# and

# ```text
# n & (n-1)   → removes the rightmost 1

