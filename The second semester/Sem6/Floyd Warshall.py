def FW(graph): #graph in matrix
    V = len(graph)
    d = [[[float('infinity')] for i in range(V)] for i in range(V)]
    
    for i in range(V):
        for j in range(V):
            if graph[i][j] != 0:
                d[i][j][0] = graph[i][j]
    
    for i in range(V):
        for j in range(V):
            for k in range(1,V):
                d[i][j][k] = min(d[i][j][k-1], (d[i][k][k-1]+d[k][j][k-1]))
                
    return d
    