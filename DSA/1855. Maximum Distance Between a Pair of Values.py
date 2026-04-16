nums1 = [55,30,5,4,2]
nums2 = [100,20,10,10,5]

# nums1 = [2,2,2]
# nums2 = [10,10,1]

# nums1 = [30,29,19,5]
# nums2 = [25,25,25,25,25]

# max_dist = 0
# for i in range(len(nums2) if len(nums1) >= len(nums2) else len(nums1)):
#     for j in range(i, len(nums2)):
#         if nums1[i] <= nums2[j]:
#             max_dist = max(max_dist, j-i)
# print(max_dist)

i=0
j=0
max_dist=0
while(j<len(nums2) and i<len(nums1)):
    if nums1[i]<=nums2[j]:
        max_dist=max(max_dist,j-i)
    else:
        i+=1
        continue
    if j==len(nums2)-2:
        j+=1
        if nums1[i]<=nums2[j]:
                max_dist=max(max_dist,j-i)
        i+=1
    else:
        j+=1
print(max_dist)