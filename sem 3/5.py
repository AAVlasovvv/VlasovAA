s = input().split()
n, m = int(s[0]), int(s[1])
#n, m = 7, 6
matrix = [[0 for i in range(n)] for i in range(m)]
print(matrix)
matrix[0][0] = 1

x, y = 0, 0
dx, dy = 1, 0
value = 2

while value <= n * m:
    if ((0 <= x + dx <= n - 1) and (0 <= y + dy <= m - 1) and (matrix[y + dy][x + dx] == 0)):
        matrix[y + dy][x + dx] = value
        #print(value)
        #print(x, dx)
        #print(y, dy)
        value += 1
        x += dx
        y += dy
        #print(x, dx)
        #print(y, dy)
        

    else:
        if dy == 1:
            dy, dx = 0, 1
        elif dx == 1:
            dx, dy = 0, -1
        elif dy == -1:
            dy, dx = 0, -1
        elif dx == -1:
            dx, dy = 0, 1

for i in range(m):
    for j in range(n):
        print(str(matrix[i][j]).ljust(3), end=" ")
    print()