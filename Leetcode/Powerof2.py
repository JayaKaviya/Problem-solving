# Given an integer n, return true if it is a power of two. Otherwise, return false.
# An integer n is a power of two, if there exists an integer x such that n == 2x. 
# Input: n = 16  #one
# Output: true
# Explanation: 2pow4 = 16 
# Input: n = 1   #two
# Output: true
# Explanation: 2pow0 = 1 
n=3
if n>1:
  for i in range(0,n//2): 
    if n==(2**i): 
      print("true") 
      break
  print("false")
else: 
  print("false")
