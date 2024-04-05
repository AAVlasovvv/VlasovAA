
def read_graph_as_edges():
    n = int(input())
    graph = [list(map(int, input().split())) for i in range(n)]
    # for i in range(n):
    #     graph.append(list(map(int, input().split())))
    return graph


def read_graph_as_neigh_list_w():
    print("На вход сначала подается одно число (q) - количество ребер. \nПотом в каждой новой строке необходимо вводить 5 чисел: \n1-е - вершина, начало ребра \n2-е - ее цвет (цвета обозначаются цифрами: различные цвета различными цифпами) \n3-е - вершина, конец ребра \n4-е - её цвет \n5-е - вес ребра")
    print("Введите количество ребер q:")
    edge_list = read_graph_as_edges()
    graph_dict = {}  # dict()
    vertex_set = set()
    for edge in edge_list:
        vertex_set.add(edge[0])
        vertex_set.add(edge[2])
    V_num = len(vertex_set)
    # # print(V_num)
    for v in vertex_set:
        graph_dict[v] = frozenset()
    for edge in edge_list:
        graph_dict[edge[0]] = graph_dict[edge[0]] | frozenset([(edge[1], edge[2], edge[3], edge[4])])
    return graph_dict


def Dijkstra(graph, v):
    d = {}
    colors = {}
    visited = []
    end = []
    for key in graph.keys():
        d[key] = float('infinity')
        colors[key] = float('infinity')
    a = 0
    d[v] = 0
    colors[v]=0
    visited.append([0, 0, v]) #1-е число - была ли смена цвета, 2-е - вес, 3-е - вершина
    while visited:
        visited.sort()
        c = visited.pop(0)
        end.append(c[2])
        for neigh in graph[c[2]]:
            list_c = list(list(graph[c[2]])[0])
            if neigh[1] not in end:
                if list_c[0] == neigh[2]:
                    colors[neigh[1]] = colors[c[2]]
                    if (d[c[2]] + neigh[3]) < d[neigh[1]]:
                        d[neigh[1]] = (d[c[2]] + neigh[3])
                    add_visited = [colors[neigh[1]], neigh[3], neigh[1]]
                    visited.append(add_visited)
                else:
                    if colors[neigh[1]] == float('inf'):
                        colors[neigh[1]] = colors[c[2]] + 1
                        if (d[c[2]] + neigh[3]) < d[neigh[1]]:
                            d[neigh[1]] = (d[c[2]] + neigh[3])
                    if colors[neigh[1]] <= colors[c[2]]:
                        continue
                    add_visited = [colors[neigh[1]], neigh[3], neigh[1]]
                    visited.append(add_visited)
                
    
    return d, colors

graph = read_graph_as_neigh_list_w()
print(graph)
print(graph[1])
d,c = Dijkstra(graph, 1)
print(d)
print(c)

'''
4
1 1 2 1 10
1 1 4 3 3
2 1 3 2 12
4 3 3 2 4
'''


'''
4
1 1 2 1 10
2 1 3 2 12
1 1 4 1 3
4 1 3 2 4
'''

'''
4
1 1 2 1 3
1 1 4 2 3
2 1 3 3 4
4 2 3 3 4
'''