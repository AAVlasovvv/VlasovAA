n, m = map(int, input().split())

dissatisfied = []

for i in range(m):
    dissatisfied.append(list(map(int, input().split())))

# print(s)

#####################################################
candidates = [1]*n
for i in range(0,n):
    candidates[i] = [1]*n
    
for i in range(0,n):
    for j in range(0, n):
        if i == j:
            candidates[i][j] = 0
# print(A)

############################################################

for i in range(0,m):
    a = dissatisfied[i][0]
    b = dissatisfied[i][1]
    candidates[a-1][b-1] = 0
    candidates[b-1][a-1] = 0

# print(A)

########################################################

def countTriangle(g, isDirected):
    nodes = len(g)
    count_Triangle = 0
    
    for i in range(nodes):
        for j in range(nodes):
            for k in range(nodes):
                
                if (i != j and i != k
                        and j != k and
                        g[i][j] and g[j][k]
                        and g[k][i]):
                    count_Triangle += 1
    
    if isDirected:
        return count_Triangle // 3
    else:
        return count_Triangle // 6


print(countTriangle(candidates, False))