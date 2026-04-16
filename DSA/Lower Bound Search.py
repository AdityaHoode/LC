arr = [1,2,3,5,9,11]
sk=-1
l=0
h=len(arr)-1
while(l<=h):
    m=(l+h)//2
    if sk > arr[m]:
        l=m+1
    else:
        h=m-1
print(l, arr[l]) if l<len(arr) else print(l)