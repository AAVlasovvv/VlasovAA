n = int(input())
projected_prices = list(map(int, input().split()))
maximum_possible_sale = [0]*n
benefit = [0]*n
profit = 0
maximum_possible_sale[-1] = projected_prices[-1]
for i in range(n-2, -1, -1):
    # print(i)
    maximum_possible_sale[i] = max(projected_prices[i], maximum_possible_sale[i+1])
# print(maximum_possible_sale)

for k in range(0, n):
    benefit[k] = maximum_possible_sale[k] - projected_prices[k]

for u in range(0, n):
    profit += benefit[u]
    
print(profit)