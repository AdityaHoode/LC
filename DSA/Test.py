# # arr = [1,2,3,11,4,5,6]
# # for i in range(1):
# #     print(i)

# # start, end = 0, len(arr)-1
# # while start<end:
# #     print(start,end)
# #     start+=1
# #     end-=1

# # print(max(arr[:4]))

# arr = [1, 2, 3, 5, 9, 11]
# sk = 12

# l = 0
# h = len(arr)
# # notice h = len(arr), not len(arr)-1

# while l < h:
#     m = (l + h) // 2
#     if arr[m] < sk:
#         l = m + 1
#     else:
#         h = m

# print("Lower bound index:", l)
# if l < len(arr):
#     print("Value at lower bound:", arr[l])
# else:
#     print("Lower bound is at end of list (no element >= search key)")

# for i in range(1):
#     print(i)

# n = [4,3,5,6]
# print(n[0:2])

# i=0
# for i in range(5):
#     if i<2:
#         continue
#     print(i)

l=[1,1,2,3,4,5,7,7,6]
s=set(l)
print(s,len(s))
