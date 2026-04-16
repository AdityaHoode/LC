# nums = [9,4,3,2]
# nums = [7,1,5,4]
# nums = [1,5,2,10]
nums = [999,997,980,976,948,940,938,928,924,917,907,907,881,878,864,862,859,857,848,840,824,824,824,805,802,798,788,777,775,766,755,748,735,732,727,705,700,697,693,679,676,644,634,624,599,596,588,583,562,558,553,539,537,536,509,491,485,483,454,449,438,425,403,368,345,327,287,285,270,263,255,248,235,234,224,221,201,189,187,183,179,168,155,153,150,144,107,102,102,87,80,57,55,49,48,45,26,26,23,15]

# i=0
# j=i+1
# max_diff = -1

# for i in range(len(nums)-1):
#     j=i+1
#     while(j<len(nums)):
#         if (nums[i] < nums[j]) and (max_diff < (nums[j]-nums[i])):
#             max_diff = nums[j]-nums[i]
#         j+=1

# print(max(max_diff,-1))

min_ele = nums[0]
max_diff = -1
for j in range(1, len(nums)):
    if nums[j] > min_ele:
        max_diff = max(max_diff, nums[j]-min_ele)
    elif nums[j] < min_ele:
        min_ele = nums[j]

print(max_diff)
