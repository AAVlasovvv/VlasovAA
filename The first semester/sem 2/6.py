A = list(map(int, input().split()))
#chet = 0
for i in range(len(A)):
    #print(A[i])
    chet = 0
    for j in range(len(A)):
        #print(A[j])
        if A[i] == A[j]:
            chet += 1
            #print(chet)
    if chet == 1:
        print(A[i])
        break
