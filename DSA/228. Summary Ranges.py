# nums = [0,1,2,4,5,7]
# ["0->2","4->5","7"]

nums = [0,2,3,4,6,8,9]
# ["0->0","2->4","6->6","8->9"]


i,j=0,1
output = []
while(j<len(nums)):
    if nums[j]-nums[j-1]==1:
        j+=1
    else:
        if j-1-i==0:
            output.append(f"{nums[i]}")
        else:
            output.append(f"{nums[i]}->{nums[j-1]}")
        i=j
        j+=1
    if j == len(nums) and nums[j-1]-nums[j-2]==1:
        output.append(f"{nums[i]}->{nums[j-1]}")
    elif j == len(nums) and nums[j-1]-nums[j-2]!=1:
        output.append(f"{nums[i]}")
print(output if output else nums)