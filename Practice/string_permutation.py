# ## String Permutation

# ### Question

# **Given a string, print all possible permutations of its characters.**

# ### Example

# **Input:**

# ```text
# ABC
# ```

# **Output:**

# ```text
# ABC
# ACB
# BAC
# BCA
# CAB
# CBA
# ```

# ### Approach

# Use **recursion + backtracking**:

# ```text
# Choose a character
#       ↓
# Put it in the current position
#       ↓
# Recursively arrange remaining characters
#       ↓
# Undo the choice
#       ↓
# Try the next character
# ```

# ### Complexity

# For a string of length `n`:

# ```text
# Number of permutations = n!
# ```

# Each permutation contains `n` characters, so printing each one takes `O(n)`.

# Therefore:

# ```text
# Time Complexity  = O(n × n!)
# Space Complexity = O(n)
# ```

# **Pattern to remember:**
# `Permutation → Recursion + Backtracking → O(n × n!)`

def permute(s,start):
    
    if len(s)==start:
        print("".join(s)) 
        return 
    
    for i in range(start,len(s)):
        
        s[start],s[i]=s[i],s[start]        
        permute(s,start+1)         
        s[start],s[i]=s[i],s[start]


s = list("ABC")
permute(s,0)