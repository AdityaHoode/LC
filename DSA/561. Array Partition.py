nums = [1,4,3,2]
sorted_nums = sorted(nums)
sum_min = 0
for i in range(0,len(nums)-1,2):
    sum_min+=sorted_nums[i]
print(sum_min)