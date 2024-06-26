def read_graph_as_edges():
    n = int(input())
    graph = [list(map(int, input().split())) for i in range(n)]
    # for i in range(n):
    #     graph.append(list(map(int, input().split())))
    return graph
def read_graph_as_neigh_list():
    edge_list = read_graph_as_edges()
    graph_dict = {} #dict()
    vertex_set = set()
    for edge in edge_list:
        vertex_set.add(edge[0])
        vertex_set.add(edge[1])
    V_num = len(vertex_set)
    # # print(V_num)
    for v in vertex_set:
        graph_dict[v] = frozenset()
    for edge in edge_list:
        if edge[0] not in graph_dict.keys():
            graph_dict[edge[0]] = frozenset([edge[1]])
            
        else:
            graph_dict[edge[0]]= graph_dict[edge[0]] | frozenset([edge[1]])
    return graph_dict

def read_graph_as_neigh_matrix():
    edge_list = read_graph_as_edges()
    vertex_set = set()
    for edge in edge_list:
        vertex_set.add(edge[0])
        vertex_set.add(edge[1])
    V_num = len(vertex_set)


    res_matrix = [[0 for i in range(V_num)]for j in range(V_num)]
    for edge in edge_list:
        index_1 = edge[0] -1
        index_2 = edge[1]-1
        res_matrix[index_1][index_2] = 1

    return res_matrix
def print_matrix(matrix):
    for line in matrix:
        print(*line)
def DFS(graph, v, visited=[]):
    print(v)
    visited.append(v)
    for neigh in graph[v]:
        if neigh not in visited:
            DFS(graph, neigh, visited)
            
    


def has_cycle(graph, v, visited=[]):
    result = False
    for neigh in graph[v]:
        if neigh in visited:
            result = True
            return result
        
        visited.append(v)
        
        if result == False:
            result = has_cycle(graph, neigh, visited)
            visited = []
    return result


def DFS_stack(graph, v, visited = []):
    
    stack = []
    
    visited.append(v)
    stack.append(v)
    while stack:
        v = stack.pop()
        print(v)
        for neigh in graph[v]:
            if neigh not in visited:
                visited.append(neigh)
                stack.append(neigh)
                
    return


# def topologicalSortUtil(graph, v, visited, stack):
#     visited[v] = True
#     for i in graph[v]:
#         if visited[i] == False:
#             topologicalSortUtil(graph, i, visited, stack)
#
#     stack.insert(0, v)
    
def topologicalSort(graph):
    V_sum = len(graph)
    visited = [False]*V_sum
    stack = []
    entry_time = [0] * (len(graph))
    exit_time = [0] * (len(graph))
    time = 1
    def topologicalSortUtil(graph, v, visited, stack):
        visited[v] = True
        nonlocal time
        entry_time[v] = time
        time += 1
        for i in graph[v]:
            if visited[i] == False:
                topologicalSortUtil(graph, i, visited, stack)
        
        exit_time[v] = time
        time += 1
        print(v, entry_time, exit_time)
        stack.insert(0, v)
    
    for i in range(V_sum):
        if visited[i] == False:
            topologicalSortUtil(graph, i, visited, stack)
            
    return stack


def count_paths(graph, start, end):
    paths = {v: 0 for v in graph}
    paths[start] = 1
    
    order: list = topologicalSort(graph)
    
    for u in order:
        for v in graph[u]:
            paths[v] += paths[u]
    
    return paths[end]
    
    
def is_the_vertex_an_ancestor(graph):
    
    entry_time = [0] * (len(graph))
    exit_time = [0] * (len(graph))
    time = 1
    def DFS(graph, vertex, visited = []):
        
        nonlocal time
        entry_time[vertex] = time
        time += 1
        
        visited.append(vertex)
        for neigh in graph[vertex]:
            if neigh not in visited:
                DFS(graph, neigh, visited)
        
        exit_time[vertex] = time
        time += 1
        # print(vertex, entry_time, exit_time)
    DFS(graph, 0)
    
    print('Введите количество запросов:')
    q = int(input())
    for i in range(q):
        v, u = map(int, input().split())
    
        if entry_time[v] < entry_time[u] and exit_time[v] > exit_time[u]:
                # print(entry_time[v], '<', entry_time[u])
                # print(exit_time[v], '>', exit_time[u])
            print('Да1')
            # elif topolog.index(v) < topolog.index(u) and entry_time[v] < entry_time[u] and exit_time[v] < exit_time[u]:
            #     print('Да2')
        else:
            print('Нет')
            

def BFS(graph, v):
    queue = []
    result = []
    d = {}
    for keys in graph.keys():
        d[keys] = 100000
    
    visited = []
    visited.append(v)
    queue.append(v)
    d[v] = 0
    
    while queue:
        u = queue.pop(0)
        print(u, end=" ")
        result.append(u)
        
        
        for neighbour in graph[u]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)
                d[neighbour] = d[u] + 1
    
    return d, result



graph = read_graph_as_neigh_list()
print(graph[2])
# print(len(graph))
print(graph)
# print_matrix(read_graph_as_neigh_matrix())
DFS(graph, 0)
# d , res = BFS(graph, 0)
# print(res)
# print(has_cycle(graph, 2))
# print(topological_sort(graph))
print(topologicalSort(graph))
# print(count_paths(graph,0,1))
is_the_vertex_an_ancestor(graph)


# print(d)

# Тесты проводил с графами:
# №1:
'''
6
0 5
0 4
5 2
2 3
3 1
4 1
'''

# №2:
'''
4
0 1
0 2
2 3
2 4
'''
'''
5
0 1
1 2
1 3
0 2
3 2
'''
'''
8
0 1
0 2
2 3
2 4
2 5
3 6
3 7
3 8
'''