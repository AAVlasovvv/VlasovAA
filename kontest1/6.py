n, k = map(int, input().split())
a = list(map(int, input().split()))
maxsum = 0
for i in range(2**n):
    j = i ^ k
    if a[i] + a[j] > maxsum:
        maxsum = a[i] + a[j]

print(maxsum)