# Question

# Find the length of the longest subarray containing at most 2 distinct numbers.

# Example
# arr = [1, 2, 1, 2, 3]

# The longest valid subarray is:

# [1, 2, 1, 2]

# It contains only 2 distinct numbers: 1 and 2.

# Answer = 4 


arr = [1, 2, 1, 2, 3]

freq = {}

left=0
maxi=0 

for right in range(len(arr)):
    
    x=arr[right] 
    freq[x]=freq.get(x,0)+1 
    
    while len(freq)>2:
        
        x=arr[left] 
        freq[x]-=1 
        
        if freq[x]==0:
            del freq[x] 
            
        left+=1
    
    maxi=max(maxi,right-left+1) 
    
print(maxi) 

# Time Complexity  = O(n)
# Space Complexity = O(n)