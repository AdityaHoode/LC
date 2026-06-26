# matrix = [
#     [1, 3, 5],
#     [7, 9, 11],
#     [13, 15, 17]
# ]

# rows = len(matrix)
# cols = len(matrix[0])

# flat_index = 5

# row = flat_index // cols
# col = flat_index % cols

# reproduce_flat_index = row * cols + col

# print(f"Flat index      : {flat_index}")
# print(f"Row             : {row}")
# print(f"Column          : {col}")
# print(f"Matrix value    : {matrix[row][col]}")
# print(f"Recreated index : {reproduce_flat_index}")

# import math
# print(math.ceil(25/11))
# print((25+11-1)//11)

# num=1234
# for n in map(int, str(num)):
#     print(n)

key="alice"
value="happy"
timestamp=1
# d=dict()
# d[key]={}
# d[key][timestamp]=value
# print(d)    

from collections import defaultdict
dd=defaultdict(dict)
dd[key][timestamp]=value
dd[key][2]="sad"
dd[key][1]="update"
print(list(dd[key].keys()))

# nums=[10,20,30]
# target=5 # 0 0 -1
# target=15 # 1 0 0
# target=25 # 2 2 1
# target=35 # 3 2 2
# l,r=0,len(nums)-1
# while l<=r:
#     m=(l+r)//2
#     if target>nums[m]:
#         l=m+1
#     elif target<nums[m]:
#         r=m-1
#     else:
#         print(f"Found: {nums[m]}")
# print(l,m,r)


# if not self.time_map[key].get(timestamp, False):
#                 recent_timestamp=max(self.time_map[key])
#                 if recent_timestamp<=timestamp:
#                     return self.time_map[key][recent_timestamp]
#                 else:
#                     return ""
#             else:
#                 return self.time_map[key][timestamp]