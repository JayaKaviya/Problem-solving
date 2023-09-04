""" Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n), 
ans[i] is the number of 1's in the binary representation of i """ 
# Input: n = 2
# Output: [0,1,1]
# Explanation:
# 0 --> 0
# 1 --> 1
# 2 --> 10

    #without bin() 
n = 2 
i=1 
cnt=0
l2=[0]  
res=0 
m=[]
while i<=n: 
    temp=i 
    p,m=[],[]
    while temp>0: 
        rem=temp%2 
        temp=temp//2 
        m.append(rem) 
    p=m[-1::-1]   
    for j in p: 
        if j==1: 
            cnt=cnt+1 
    l2.append(cnt)
    i+=1 
    cnt=0 
print(l2) 

    #with bin() 
        # i=1 
        # cnt=0
        # l2=[0]
        # while i<=n:
        #   c=bin(i) 
        #   l=list(c)  
        #   l1=l[2:] 
        #   #print(l1)  
        #   for j in l1: 
        #     if int(j)==1: 
        #        cnt=cnt+1 
        #   l2.append(cnt)
        #   i+=1 
        #   cnt=0 
        # return l2 




   