def fn():
    n=0
    if n==0:
        return 0
    nums=[0,1]
    i=1
    flag=1
    while(flag):
        if (2*i>=2 and 2*i<=n):
            nums.append(nums[i])
        else:
            flag=0
        if (2*i+1>=2 and 2*i+1<=n):
            nums.append(nums[i] + nums[i + 1])
            flag=1
        else:
            flag=0
        i+=1
    return nums, max(nums)

print(fn())