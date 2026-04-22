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

# l=[1,1,2,3,4,5,7,7,6]
# s=set(l)
# print(s,len(s))

# for i in range(1,3):
#     print(i)

# l=[1,2,3,4,5,6]
# print(l[2:].index(4))

# from collections import Counter
# d={'act': Counter({'a': 1, 'c': 1, 't': 1}), 'pots': Counter({'p': 1, 'o': 1, 't': 1, 's': 1}), 'tops': Counter({'t': 1, 'o': 1, 'p': 1, 's': 1}), 'cat': Counter({'c': 1, 'a': 1, 't': 1}), 'stop': Counter({'s': 1, 't': 1, 'o': 1, 'p': 1}), 'hat': Counter({'h': 1, 'a': 1, 't': 1})}
# for k,v in d.items():
#     print(k,v)

# l=['vbg','fgr','dsa']
# sl=[''.join(sorted(i)) for i in l]
# print(sl)

# l1=[""]
# l2=[]
# o1a=' '.join(l1)
# o1b=o1a.split()
# o2a=' '.join(l2)
# o2b=o2a.split()
# print(o1a)
# print(o1b)
# print('------------------------------')
# print(o2a)
# print(o2b)

s="3#adi3#hoo"
s1=""
print(s[1:2])