# Next Greater Element to the Right

# Given an array, find the first greater element on the right for each element. 
# If no greater element exists, return -1.

# Example:

# arr = [4, 5, 2, 10, 8]

# Output:

# [5, 10, 10, -1, -1] 


arr = [4, 5, 2, 10, 8]

n = len(arr)
result = [-1] * n
stack = []

for i in range(n - 1, -1, -1):
    while stack and stack[-1] <= arr[i]:
        stack.pop()

    if stack:
        result[i] = stack[-1]

    stack.append(arr[i])

print(result) 


# Complexity

# Time Complexity: O(n) — each element is pushed and popped at most once.

# Space Complexity: O(n) — the stack and result array use extra space.

# Pattern: Monotonic Stack (Next Greater Element).