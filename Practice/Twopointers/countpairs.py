# Given an array of integers, find the number of pairs (i, j) such that:

# i < j
# arr[i] + arr[j] = 1

# Return the count of such pairs.

# Example
# arr = [3, -2, 5, -4, 1, 0, 2, -1]

# Valid pairs:

# -4 + 5 = 1
# -1 + 2 = 1
# 0 + 1 = 1

# Answer:

# 3 

arr = [3, -2, 5, -4, 1, 0, 2, -1]

arr.sort()

left = 0
right = len(arr) - 1
count = 0

while left < right:

    total = arr[left] + arr[right]

    if total == 1:
        count += 1
        left += 1
        right -= 1

    elif total < 1:
        left += 1

    else:
        right -= 1

print(count)
 
 
# Complexity:
# Operation	Complexity
# Sorting	O(n log n)
# Two-pointer scan	O(n)
# Total	O(n log n)
# Extra space	O(1)*

# *Assuming the sorting is in-place.

# Pattern to remember

# When you see:

# Pair + target sum + sorted array




# Approach Used: Two Pointers

# First, sort the array.

# Then use two pointers:

# left  → beginning
# right → end

# Because the array is sorted:

# If arr[left] + arr[right] < 1
# → sum is too small → move left forward to get a bigger value.
# If arr[left] + arr[right] > 1
# → sum is too large → move right backward to get a smaller value.
# If sum is exactly 1
# → pair found → move both pointers.