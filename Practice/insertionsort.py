arr=[64, 34, 25, 12, 22, 11, 90, 5]

n=len(arr) 
k=-1
for i in range(1,n):
    
    key=arr[i]    
    for j in range(i-1,-1,-1):
     if arr[j]>key:
        arr[j+1]=arr[j] 
        k=j
     else:
        break
    if k!=-1:
        arr[k]=key
        k=-1
 
print(arr)