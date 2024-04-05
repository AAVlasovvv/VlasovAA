import pylab as p
from heapq import *
def read_graph_as_edges():
    n = int(input())
    graph = [list(map(int, input().split())) for i in range(n)]
    # for i in range(n):
    #     graph.append(list(map(int, input().split())))
    return graph

def read_graph_as_neigh_list_w():
    edge_list = read_graph_as_edges()
    graph_dict = {}  # dict()
    vertex_set = set()
    for edge in edge_list:
        vertex_set.add(edge[0])
        vertex_set.add(edge[1])
    V_num = len(vertex_set)
    # # print(V_num)
    for v in vertex_set:
        graph_dict[v] = frozenset()
    for edge in edge_list:
        
            graph_dict[edge[0]] = graph_dict[edge[0]] | frozenset([(edge[1], edge[2])])
    return graph_dict

def read_graph_as_neigh_matrix():
    edge_list = read_graph_as_edges()
    vertex_set = set()
    for edge in edge_list:
        vertex_set.add(edge[0])
        vertex_set.add(edge[1])
    V_num = len(vertex_set)
    
    res_matrix = [[0 for i in range(V_num)] for j in range(V_num)]
    for edge in edge_list:
        index_1 = edge[0] - 1
        index_2 = edge[1] - 1
        res_matrix[index_1][index_2] = edge[1]
    
    return res_matrix

def read_graph_as_neigh_matrix_w():
    edge_list = read_graph_as_edges()
    vertex_set = set()
    for edge in edge_list:
        vertex_set.add(edge[0])
        vertex_set.add(edge[1])
    V_num = len(vertex_set)
    
    res_matrix = [[0 for i in range(V_num)] for j in range(V_num)]
    for edge in edge_list:
        index_1 = edge[0] - 1
        index_2 = edge[1] - 1
        res_matrix[index_1][index_2] = edge[2]
    
    return res_matrix

def print_matrix(matrix):
    for line in matrix:
        print(*line)

def Dijkstra(graph, v):
    d = {}
    visited = []
    end = []
    for key in graph.keys():
        d[key] = float('infinity')
        
    d[v] = 0
    visited.append([0, v])
    while visited:
        visited.sort()
        
        c = visited.pop(0)
        end.append(c[1])
        for neigh in graph[c[1]]:
            print(neigh)
            if neigh[0] not in end:
                if (d[c[1]] + neigh[1]) < d[neigh[0]]:
                    d[neigh[0]] = (d[c[1]] + neigh[1])
                visited.append(neigh[::-1])
                print('visited',visited)
    
    return d


def Floyd_Warshall(graph):
    v = len(graph)
    d = [[ float('infinity') for i in range(v)]for j in range(v)]
    nxt = [[-1 for i in range(v)] for j in range(v)]
    for i in range(v):
        for j in range(v):
            if graph[i][j] != 0:
                d[i][j] = graph[i][j]
                nxt[i][j] = j
    for k in range(1, v):
        for i in range(v):
            for j in range(v):
                if d[i][k]+d[k][j] < d[i][j]:
                    d[i][j] = d[i][k] + d[k][j]
                    nxt[i][j] = nxt[i][k]

    return d, nxt

def pth(i, j, nxt):
    # i = nxt[i][j]
    p = [i]
    while nxt[i-1][j-1] + 1 != j:
        i = nxt[i-1][j-1] + 1
        p.append(i)
    p.append(j)
    return p

def kruskal(graph): # read_graph_as_edges
    g = graph
    for e in g:
        e[0], e[2] = e[2], e[0]
    g.sort()
    tree_v = set()
    tree_e = []
    for e in g:
        if e[1] not in tree_v or e[2] not in tree_v:
            tree_v.add(e[1])
            tree_v.add(e[2])
            tree_e.append(e)
        else:
            continue
    return tree_e


def prim(graph):  # read_graph_as_neigh_list_w
    
    v = 1
    tmp = list(graph[v])
    h = []
    
    for e in tmp:
        h.append([e[1], e[0], v])
    heapify(h)
    tree_v = set([v])
    tree_e = []
    
    while h:
        e_min = heappop(h)
        if e_min[1] not in tree_v:
            tree_v.add(e_min[1])
            for e in graph[e_min[1]]:
                t = [e[1], e[0]]
                heappush(h, (list(t) + [e_min[1]]))
            v = e_min[1]
            tree_e.append(e_min)
        else:
            continue
    
    return tree_e




graph = read_graph_as_neigh_list_w()
b = Dijkstra(graph, 1)
# print(graph)
# print(list(list(graph[1])[0]))
print(b)
#
# E = kruskal(graph)
# print(E)




'''
8
1 4 6
1 2 1
3 2 2
2 5 3
2 6 1
5 3 1
6 2 2
6 4 1
'''
'''
5
1 2 1
2 4 1
4 3 1
2 3 4
1 3 6
'''

''' {1: 0, 2: 1, 3: 3, 4: 2} '''

'''
8
8 1 5
1 2 1
1 3 2
1 4 3
2 5 20
3 5 6
3 6 5
4 6 10
'''
''' {1: 0, 2: 1, 3: 2, 4: 3, 5: 8, 6: 7, 8: inf} '''

'''
8
8 1 5
1 2 20
1 3 2
1 4 3
2 5 1
3 5 6
3 6 5
4 6 10
'''

'''
10
1 2 3
1 3 6
2 4 2
2 5 5
3 4 7
4 5 1
5 6 8
4 6 11
3 7 9
7 6 10
'''