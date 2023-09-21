A = list(map(int, input().split()))
chetM = 0
for i in range(len(A)):
    #print(A[i])
    chet = 0
    for j in range(len(A)):
        #print(A[j])
        if A[i] == A[j]:
            chet += 1
            
    if chet >= chetM:
        chetM = chet
        M = A[i]
print(M)
