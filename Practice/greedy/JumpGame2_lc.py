# 1.Jump Game 2 - Minimum Jumps to Reach the End ⭐⭐⭐⭐⭐
# Question

# You are given an array where:

# nums[i] tells you the maximum number of positions you can jump forward from index i.

# Find the minimum number of jumps needed to reach the last index.

# Example
# nums = [2, 3, 1, 1, 4]

# Indexes:

# index:  0  1  2  3  4
# value:  2  3  1  1  4

# Minimum path:

# 0 → 1 → 4

# So:

# Answer = 2 


class Solution:
    def jump(self, nums):
        jumps = 0
        left = 0
        right = 0

        while right < len(nums) - 1:
            farthest = 0

            for i in range(left, right + 1):
                farthest = max(farthest, i + nums[i])

            left = right + 1
            right = farthest
            jumps += 1

        return jumps 
    
# We keep track of:

# jumps → how many jumps we have made
# left, right → indexes we can consider with the current jumps
# farthest → the farthest index we can reach with one more jump

# For:

# [2, 3, 1, 1, 4]

# First:

# 0 → can reach up to 2

# Then we check indexes 1 and 2.

# index 1 + value 3 = 4
# index 2 + value 1 = 3

# Farthest = 4.

# So:

# 0 → 1 → 4

# jumps = 2.

# Complexity

# Time: O(n)

# Space: O(1) 
#------------------------------------------------------------

# 2. Jump Game : 
    
    
# You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.

# Return true if you can reach the last index, or false otherwise.

 

# Example 1:

# Input: nums = [2,3,1,1,4]
# Output: true
# Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
# Example 2:

# Input: nums = [3,2,1,0,4]
# Output: false
# Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.
 

# Constraints:

# 1 <= nums.length <= 104
# 0 <= nums[i] <= 105 

class Solution:
    def canJump(self, nums: list[int]) -> bool:
        left = 0
        right = 0

        while right < len(nums)-1:
            
            farthest=0 
            for i in range(left,right+1):
                farthest=max(farthest,i+nums[i])
                
            if farthest <=right:
                return False
            
            left=right+1
            right=farthest
             
        return True 
    
# Complexity

# Time Complexity: O(n)

# Even though there is a while loop and a for loop, each index is processed only as part of the expanding reachable range, so the total work is linear.

# Space Complexity: O(1) 

# Simple Explanation

# We keep track of:

# right → the farthest index we can currently reach
# farthest → the farthest index we can reach from the indexes we are checking

# For:

# index:   0  1  2  3  4
# value:   3  2  1  0  4

# From index 0:

# 0 + 3 = 3

# So we can reach index 3.

# Now check indexes 1, 2, 3:

# 1 + 2 = 3
# 2 + 1 = 3
# 3 + 0 = 3

# So:

# farthest = 3
# right = 3

# We did not move beyond 3.

# Therefore:

# farthest <= right

# is:

# 3 <= 3  → True

# We are stuck, so:

# return False
# Why i + nums[i]?

# Because:

# i = current index
# nums[i] = maximum distance we can move

# So:

# current index + distance = destination index

# For example:

# index 1
# value 3

# means:

# 1 + 3 = 4

# So we can reach index 4.
    
        