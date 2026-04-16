from collections import defaultdict, OrderedDict
nums = [4,2,1,2]
p = 1
flag=0
diff=[]
max_diff=0
nums.sort()
print(nums)
d = defaultdict(list)
for i in range(0,len(nums)-1,1):
    d[abs(nums[i]-nums[i+1])].append([nums[i],nums[i+1]])
sorted_d = OrderedDict(sorted(d.items()))
print(sorted_d)
for k,v in sorted_d.items():
    for j in range(len(v)):
        diff.append(abs(v[j][0]-v[j][1]))
        flag+=1

print(d, diff, max(diff[:p]))