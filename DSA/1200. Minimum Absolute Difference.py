arr = [4,2,1,3]
arr.sort()
min_diff=0
output=[]
for i in range(0,len(arr)-1,1):
    if not min_diff >= (arr[i+1]-arr[i]):
        min_diff = arr[i+1]-arr[i]
        output.append([arr[i],arr[i+1]])
print(output)