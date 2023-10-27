n, k = map(int, input().split())
a = list(map(int, input().split()))
mx = -1
for i in range(2 ** n):
    j = i ^ k
    if a[i] + a[j] > mx:
        mx = a[i] + a[j]
        
print(mx)