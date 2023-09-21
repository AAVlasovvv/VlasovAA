A = list(map(int, input().split()))
#print(A)
for i in range(len(A)-1):
    #print(A[i])
    A[-i], A[-i-1] = A[-i-1], A[-i]
    #print(A[i])
print(' '.join(map(str, A)))
