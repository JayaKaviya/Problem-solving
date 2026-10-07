# ## Merge Overlapping Intervals — Question

# > **Given a collection of intervals, merge all overlapping intervals 
# and return the resulting non-overlapping intervals.**

# ### Example

# ```text
# Input:
# [[1,3], [2,6], [8,10], [9,12]]
# ```

# Here:

# ```text
# [1,3] overlaps [2,6]
# ```

# so they become:

# ```text
# [1,6]
# ```

# And:

# ```text
# [8,10] overlaps [9,12]
# ```

# so they become:

# ```text
# [8,12]
# ```

# ### Output

# ```text
# [[1,6], [8,12]]
# ```

# ### Approach

# **Sorting + interval merging**

# ### Complexity

# ```text
# Time  : O(n log n)
# Space : O(n)
# ``` 


intervals = [[1, 3], [2, 6], [8, 10], [9, 12]]

intervals.sort()

result = []

for start, end in intervals:

    if not result or start > result[-1][1]:
        result.append([start, end])

    else:
        result[-1][1] = max(result[-1][1], end)

print(result)
