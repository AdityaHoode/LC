arr = [1,2,3,5,9,11]
sk=8
flag=0
l=0
h=len(arr)-1
while(l<=h):
    m=(l+h)//2
    if arr[m]==sk:
        print("Found: ", m)
        flag=1
        break
    elif sk > arr[m]:
        l=m+1
    else:
        h=m-1
if not flag:
    print("Not found")
