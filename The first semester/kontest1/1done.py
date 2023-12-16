BI = list(map(int, input().split()))
CB = []
if len(BI) > 2:
    CB.append(BI[0])
    CB.append(BI[1])
    for i in range(2, len(BI)):
        CB.append(max(CB[i-1], BI[i]+CB[i-2]))
    RB = CB[-1]
elif len(BI) == 2:
    RB = max(BI[0], BI[1])
else:
    RB = BI[0]
print(RB)