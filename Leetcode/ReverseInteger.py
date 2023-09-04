# Example 1:
# Input: x = 123
# Output: 321
# Example 2:
# Input: x = -123
# Output: -321 
# [-231, 231 - 1], then return 0.

x =1534236469 
#output: 0 
j=pow(-2,31) 
k=pow(2,31)-1
y=str(x) 
print( j , k)
if x<0: 
    m='-' 
    n=y[1:]
    a=int(n[-1::-1]) 
    if j<a and a<k : 
        print(-a) 
    else:
        print(0) 
else: 
    a=int(y[-1::-1])
    if j<a and a<k :  
        print(a) 
    else:
        print(0)