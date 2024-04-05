# a = input("Введите массив чисел через пробел: \n")
# A = list(map(float, a.split()))
q = int(input("Введите количество ограничений: "))
print("В каждой строке введите через пробел числа l, r и выражение с k (>k \ <k")
array_of_boundaries = [list(map(str, input().split())) for i in range(q)]
result = True
for i in range(q):
    l = int(q[i][0])
    r = int(q[i][1])
    
    
