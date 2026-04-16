prices = [7,1,5,3,6,4]

bl = prices[0]
sh = -1
profit = 0

for j in range(len(prices)):
    sh = prices[j]
    if bl > sh:
        bl = sh
    else:
        profit = max(profit, sh - bl)

print(profit)