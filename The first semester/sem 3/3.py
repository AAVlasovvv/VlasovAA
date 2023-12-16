A = list(map(int, input().split()))
x, y = A[0], A[1]


def NOD(a, b):
    while a != 0 and b != 0:
        if a > b:
            a = a % b
        else:
            b = b % a
    return (a + b)

x1 = x / NOD(x, y)
y1 = y / NOD(x, y)
x_min = int(min(x1, y1))
y_max = int(max(x1, y1))

ans_1 = y_max % x_min
if ans_1 == 0:
    
    ans_1 = 1
    ans_2 = 0
else:
    ans_2 = ans_1 - x_min

print(ans_2, ans_1, NOD(x, y))
