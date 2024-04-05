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


def AntiDijkstra(graph, v):
    # в этой функции выводиться минимальное ребро на самом неоптимальном пути, т.е.
    # Я также ищу самый длинный путь, но вывожу не вес всего пути, а вес самого лекгого ребра
    d = {}
    w = {}
    visited = []
    end = []
    for key in graph.keys():
        d[key] = float('-inf')
        w[key] = float('inf')
    d[v] = 0
    # w[v] = 0
    visited.append([0, v])
    while visited:
        visited.sort()
        c = visited.pop(-1)
        end.append(c[1])
        for neigh in graph[c[1]]:
            # if neigh[0] not in end:
                if (d[c[1]] + neigh[1]) > d[neigh[0]]:
                    d[neigh[0]] = (d[c[1]] + neigh[1])
                    if w[c[1]] > neigh[1]:
                            w[neigh[0]] = neigh[1]
                    else:
                        w[neigh[0]] = w[c[1]]

                visited.append(neigh[::-1])

    # for key in d:
    #     if d[key] == 0:
    #         d[key] = float('infinity')
        # if w[key] == float('infinity'):
        #     w[key] = '_'

   
    return d, w
    
    


graph = read_graph_as_neigh_list_w()
d, w = AntiDijkstra(graph, 1)
print(graph)
print(d)
print(w)

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

''' {1: 0, 2: 1, 3: 2, 4: 3, 5: 21, 6: 13, 8: -inf}
{1: inf, 2: 1, 3: 2, 4: 3, 5: 1, 6: 3, 8: inf}'''


'''{1: 0, 2: 20, 3: 2, 4: 10, 5: 21, 6: 13, 8: -inf}
{1: inf, 2: 20, 3: 2, 4: 10, 5: 1, 6: 3, 8: inf}'''
'''
8
8 1 5
1 2 20
1 3 2
1 4 10
2 5 1
3 5 6
3 6 5
4 6 3
'''
