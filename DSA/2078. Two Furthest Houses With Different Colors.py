colors = [1,8,3,8,3]
max_dist = 0

# for i in range(len(colors)-1):
#     fh = colors[i]
#     for j in range(i+1, len(colors)):
#         if colors[j] != fh:
#             max_dist=max(max_dist,j-i)
# print(max_dist)

dist1,dist2 = 0

eh = colors[len(colors)-1]
for j in range(len(colors)-1):
    if eh != colors[j]:
        dist1 = j

sh = colors[0]
for j in range(len(colors)-2, 0, -1):
    if sh != colors[j]:
        dist2 = j

print(max(dist1, dist2))

