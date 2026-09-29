# Maximum Sum Subarray of Size K ⭐⭐⭐⭐⭐

# This is the fixed-size sliding window.

# Question

# Given an array and K, find the maximum sum of any contiguous subarray of size K.

# Example
# arr = [2, 1, 5, 1, 3, 2]
# K = 3

# Possible windows:

# [2, 1, 5] → 8
# [1, 5, 1] → 7
# [5, 1, 3] → 9
# [1, 3, 2] → 6

# Answer:

# 9

arr = [2, 1, 5, 1, 3, 2]
k = 3

win_sum=sum(arr[:k]) 
maxi=win_sum 

for i in range(k,len(arr)):
    
    win_sum+=arr[i] 
    
    win_sum-=arr[i-k]
    
    maxi=max(maxi,win_sum) 
    
print(maxi) 


# Complexity
# Time  : O(n)
# Space : O(1)