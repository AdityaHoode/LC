intervals = [[3,4],[2,3],[1,2]]

sorted_start_j = sorted([[x[0],i] for i,x in enumerate(intervals)])

output = []

for _,sk in intervals:
    l=0
    h=len(sorted_start_j)-1
    while(l<=h):
        m=(l+h)//2
        if sk > sorted_start_j[m][0]:
            l=m+1
        else:
            h=m-1
    if l<len(sorted_start_j):
        output.append(sorted_start_j[l][1])
    else:
        output.append(-1)

print(output)
