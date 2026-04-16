nums= [9,4,1,7]
k = 2
nums.sort()
# print(max(nums[-k:])-min(nums[-k:]))
if len(nums)==1:
    print(0)
nums.sort()
diff=10**5
for i in range(len(nums)-k+1):
    diff=min(diff,abs(nums[i]-nums[i+k-1]))
print(diff)