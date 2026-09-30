# ## Minimum Cost to Connect Ropes — Greedy

# ### Question

# Given an array of rope lengths, connect all the ropes into **one rope**.

# Whenever you connect two ropes, the cost is:

# ```text
# cost = length of rope 1 + length of rope 2
# ```

# Find the **minimum total cost** required to connect all the ropes.

# ### Example

# ```python
# ropes = [4, 3, 2, 6]
# ```

# Greedy approach:

# ```text
# 2 + 3 = 5    → cost = 5
# 4 + 5 = 9    → cost = 9
# 6 + 9 = 15   → cost = 15
# ```

# Total:

# ```text
# 5 + 9 + 15 = 29
# ```

# **Output:**

# ```text
# 29
# ```

# ### Approach

# Use a **min-heap**:

# 1. Put all ropes into a min-heap.
# 2. Remove the two smallest ropes.
# 3. Add them and add their sum to the total cost.
# 4. Put the new combined rope back into the heap.
# 5. Repeat until only one rope remains.

# ### Complexity

# There are `n - 1` combinations.

# Each `heappop()` and `heappush()` takes `O(log n)`.

# Therefore:

# ```text
# Time Complexity  : O(n log n)
# Space Complexity : O(n)
# ```

# **Pattern to remember:**

# ```text
# Minimum total cost
#         ↓
# Repeatedly choose smallest elements
#         ↓
# Greedy + Min Heap
# ```
 
 
import heapq

ropes = [4, 3, 2, 6]
heapq.heapify(ropes)  
cost=0
while len(ropes)>1:
    
    a=heapq.heappop(ropes)
    b=heapq.heappop(ropes)
    
    total=a+b 
    cost+=total
    heapq.heappush(ropes,total) 
    
print(cost)
