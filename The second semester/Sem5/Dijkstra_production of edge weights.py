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


def Dijkstra(graph, v):
    d = {}
    visited = []
    end = []
    for key in graph.keys():
        d[key] = float('infinity')
    
    d[v] = 1
    visited.append([0, v])
    while visited:
        visited.sort()
        
        c = visited.pop(0)
        end.append(c[1])
        for neigh in graph[c[1]]:
            if neigh[0] not in end:
                if (d[c[1]] * neigh[1]) < d[neigh[0]]:
                    d[neigh[0]] = (d[c[1]] * neigh[1])
                visited.append(neigh[::-1])
                
    d[v] = 0
    
    return d


graph = read_graph_as_neigh_list_w()
b = Dijkstra(graph, 1)
print(graph)
print(b)

'''
7
1 2 1
1 3 2
1 4 3
2 5 20
3 5 6
3 6 5
4 6 10
'''