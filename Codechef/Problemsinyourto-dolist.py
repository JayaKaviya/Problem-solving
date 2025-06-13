#Problems in your to-do list 

t=int(input()) 
l=[]
for i in range(t):
    n=input().split()
    x=list(map(int,input().split()))
    l.append(x) 

for i in l: 
    tot=0
    for j in i:
        if j>=1000:
            tot+=1 
    print(tot)
            
        