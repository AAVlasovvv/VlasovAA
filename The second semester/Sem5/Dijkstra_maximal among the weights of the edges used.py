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


def Dijkstra1(graph, v):
    #тут я просто искал пусть от v к u, такой чтобы он содержал максимальный отрезок, и выводил его,
    #далее будет Дейкстра, типа как минимальный путь, но выводиться будет максимальное ребро с оптимального пути
    d = {}
    visited = []
    end = []
    for key in graph.keys():
        d[key] = 0
    
    d[v] = 0
    visited.append([0, v])
    while visited:
        visited.sort()
        c = visited.pop(-1)
        end.append(c[1])
        for neigh in graph[c[1]]:
            if neigh[0] not in end:
                if (d[c[1]] + neigh[1]) > d[neigh[0]]:
                    if d[c[1]] < neigh[1]:
                        d[neigh[0]] = (neigh[1])
                    else:
                        d[neigh[0]] = d[c[1]]
                visited.append(neigh[::-1])
    
                
    for key in d:
        if d[key] == 0:
            d[key] = float('infinity')
            
    d[v] = 0
    print(visited)
    return d


# def Dijkstra2(graph, v):
#     #в этой функции выводиться максимальное ребро на оптимальном пути, т.е.
#     #Я также ищу самый короткий путь, но вывожу не вес всего пути, а вес самого тяжелого ребра
#     d = {}
#     visited = []
#     end = []
#     w = {}
#     for key in graph.keys():
#         d[key] = float('infinity')
#         w[key] = 0
#
#     d[v] = 0
#     visited.append([0, v])
#     while visited:
#         visited.sort()
#         c = visited.pop(0)
#         end.append(c[1])
#         for neigh in graph[c[1]]:
#             if neigh[0] not in end:
#                 if (d[c[1]] + neigh[1]) < d[neigh[0]]:
#                     d[neigh[0]] = (d[c[1]] + neigh[1])
#                     if w[neigh[0]] < neigh[1]:
#                         w[neigh[0]] = neigh[1]
#                 visited.append(neigh[::-1])
#
#     return w





graph = read_graph_as_neigh_list_w()
b = Dijkstra1(graph, 1)
# w = Dijkstra2(graph, 1)
print(graph)
print(b)
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
'''{1: 0, 2: 1, 3: 2, 4: 3, 5: 20, 6: 10, 8: inf}'''
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
'''{1: 0, 2: 20, 3: 2, 4: 10, 5: 20, 6: 10, 8: 0} '''