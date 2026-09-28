# Given a string, repeatedly remove adjacent equal characters.

# Example:

# Input:
# "abbaca"

# Step 1:
# abbaca
#  ↓
# aaca

# Step 2:
# aaca
#  ↓
# ca

# Output:
# "ca" 


s = "abbaca"

stack=[] 

for ch in s:
    
    if stack and stack[-1]==ch:
        stack.pop() 
    else:
        stack.append(ch) 
print("".join(stack))