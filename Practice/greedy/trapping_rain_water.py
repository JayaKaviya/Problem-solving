# Trapping Rain Water ⭐⭐⭐⭐⭐
# Question

# You are given an array where each number represents the height of a bar. Each bar has width 1.

# After raining, find the total amount of water trapped between the bars.

# Example:

# height = [4, 2, 0, 3, 2, 5]

# Water trapped:

# index 1 → 2 units
# index 2 → 4 units
# index 3 → 1 unit
# index 4 → 2 units

# Total = 9
# Approach Used
# Two Pointer + Greedy approach

# We use two pointers:

# left →                 ← right
# [4, 2, 0, 3, 2, 5]

# We also keep:

# left_max  = tallest bar seen from left
# right_max = tallest bar seen from right
# Main idea

# Water at a position depends on the shorter boundary:

# water = min(left_max, right_max) - current_height

# So:

# If height[left] <= height[right] → process left
# Otherwise → process right 


class Solution:
    def trap(self, height):
        left = 0
        right = len(height) - 1

        left_max = 0
        right_max = 0

        water = 0

        while left < right:

            if height[left] <= height[right]:

                if height[left] >= left_max:
                    left_max = height[left]
                else:
                    water += left_max - height[left]

                left += 1

            else:

                if height[right] >= right_max:
                    right_max = height[right]
                else:
                    water += right_max - height[right]

                right -= 1

        return water 
    
# Complexity

# Time: O(n)

# Each position is processed once.

# Space: O(1)

# Only a few variables are used; no extra array.

# Remember

# Approach = Two Pointers + Greedy

# Shorter boundary decides the water level.