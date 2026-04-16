arr = [17,18,5,4,6,1]

# for i in range(len(arr)-1):
#     rmax = max(arr[i+1:])
#     arr[i] = rmax
# arr[-1] = -1
# print(arr)

# i=0
# for j in range(len(arr)-1, -1, -1):
#     if i<j:
#         lmax = max(arr[i+1:])
#         arr[i] = lmax
#         i+=1
#     else:
#         break
# arr[-1] = -1
# print(arr)

rmax = -1
for i in range(len(arr)-1, -1, -1):
    new_val = rmax
    rmax = max(rmax, arr[i])
    arr[i] = new_val
print(arr)