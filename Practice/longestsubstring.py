# Longest Substring Without Repeating Characters ⭐⭐⭐⭐⭐

# This is the most important variable-size sliding window problem.

# Question

# Find the length of the longest substring containing no repeated characters.

# Example
# s = "abcabcbb"

# Possible windows:

# abc → 3
# bca → 3
# cab → 3

# Answer:

# 3 

s = "abcabcbb" 
seen=set() 
left=0 
maxi=0

for right in range(len(s)): 
    while s[right] in seen:
        seen.remove(s[left])
        left+=1 
    seen.add(s[right])  
    maxi=max(maxi,right-left+1) 
    
print(maxi)
        
        
# Time Complexity  = O(n)
# Space Complexity = O(n)