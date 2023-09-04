# Given an integer num, repeatedly add all its digits until the result has only one digit, and return it.
# Input: num = 38
# Output: 2
# Explanation: The process is
# 38 --> 3 + 8 --> 11
# 11 --> 1 + 1 --> 2 
# Since 2 has only one digit, return it. 
num,sum=38,0
if num in (0,1,2,3,4,5,6,7,8,9): 
    print(num) 
else: 
    l=list(str(num))
    print(l) 
    while len(l)>1: 
        for i in l: 
           sum=sum+int(i) 
        if sum in (0,1,2,3,4,5,6,7,8,9): 
           print(sum)  
           break 
        l,sum=list(str(sum)),0
        print(l)
    print(sum)
