list1 = list(map(int, input().split()))
list2 = list(map(int, input().split()))
print("уникальные в 1 множестве", set(list1))
print("уникальные во 2 множестве", set(list2))# объединение
set_un = set.union(set(list1), set(list2))# пересечение
set_int = set.intersection(set(list1), set(list2))
print("только уникальные в 2", set.difference(set_un, set_int))
print("совпадающие в двух", set_int)