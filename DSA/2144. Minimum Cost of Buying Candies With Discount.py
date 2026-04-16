cost = [10,5,9,4,1,9,10,2,10,8]
cost.sort(reverse=True)
freebie=0
for i in range(2, len(cost), 3):
    freebie+=cost[i]
print(sum(cost)-freebie)