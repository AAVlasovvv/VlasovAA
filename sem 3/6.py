import numpy as np

numbers = list(map(int, input().split()))
x, y = numbers[0], numbers[1]
def mnk(x, y):
    size = len(x)
    
    vec = np.empty((2, 1))
    vec[0] = sum((x[i] * y[i]) for i in range(0, size))
    vec[1] = sum((y[i]) for i in range(0, size))
    
    matr = np.empty((2, 2))
    matr[[0], [0]] = sum((x[i]) ** 2 for i in range(0, size))
    matr[[0], [1]] = sum(x)
    matr[[1], [0]] = sum(x)
    matr[[1], [1]] = size
    
    opposite = np.linalg.inv(A)
    
    ab = np.dot(opposite, vec)
    a = ab[0]
    b = ab[1]
    
    return a, b

print(x,y)