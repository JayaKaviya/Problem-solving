#Maximum Difference Between Adjacent Elements in a Circular Array 

nums=[-3,-4,2]
maximum=0
for i in range(0,len(nums)):
    if i<len(nums)-1:
        diff =abs(nums[i]-nums[i+1])
        print("diff",diff)
        if diff > maximum : 
            maximum=diff 
    else:
        diff =abs(nums[-1]-nums[0])
        diff2=abs(nums[0]-nums[-1])
        print(diff,diff2,maximum)
        if max(diff,diff2)>maximum:
            maximum=max(diff,diff2)
print(maximum)
        