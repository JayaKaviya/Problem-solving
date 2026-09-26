#Finding the count of peak elements in an array where the Xor sum of left 
# and right side elements are less than the peak element
#here took count, if you want elemnt, just print it

arr = [4, 2, 7, 3, 6]
n = len(arr)
prefix = [0] * n
suffix = [0] * n
for i in range(1, n):
    prefix[i] = prefix[i - 1] ^ arr[i - 1]

for i in range(n - 2, -1, -1):
    suffix[i] = suffix[i + 1] ^ arr[i + 1]
count = 0
for i in range(n):
    if prefix[i] < arr[i] and suffix[i] < arr[i]:
        count += 1 
        
#if you want to skip first and last elements :
# for i in range(1, n - 1):
#     if prefix[i] < arr[i] and suffix[i] < arr[i]:
#         count += 1
print(count) 


