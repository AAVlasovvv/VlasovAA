import pylab as p
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

def Bellman_Ford(graph, v):
    vertices = len(graph)
    distance = {vertex: float('inf') for vertex in graph}
    distance[v] = 0
    for _ in range(vertices - 1):
        for vertex in graph:
            for neighbor, weight in graph[vertex]:
                if distance[vertex] != float('inf') and distance[vertex] + weight < distance[neighbor]:
                    distance[neighbor] = distance[vertex] + weight
    for vertex in graph:
        for neighbor, weight in graph[vertex]:
            if distance[vertex] != float('inf') and distance[vertex] + weight < distance[neighbor]:
                print("Граф сдержит отрицательный цикл")
                return

    return distance
            
            
            
                
graph = read_graph_as_neigh_list_w()
f = Bellman_Ford(graph,1)
print(f)

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

'''
8
1 2 -1
2 3 2
3 4 -3
4 5 5
1 5 4
2 5 3
2 4 2
4 2 1
'''

'''
10
0 1 6
1 2 5
2 1 -2
3 2 7
4 3 9
0 4 7
1 4 -8
4 2 -3
3 0 2
1 3 -4
'''