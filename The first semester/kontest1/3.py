prohod = list(map(int, input().split()))
n = int(prohod[0])
m = int(prohod[1])
mines = 0
i = 0
delta = 0
while (n % 2 != 0) and (m % 2 != 0):
    delta = 4**i
    mines += delta
    i += 1
    n = (n-1)/2
    m = (m-1)/2
print(mines)
