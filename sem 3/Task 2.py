import numpy as np

N = int(input())

sqr = np.sqrt(N)
print(int(sqr))
dividers = []
for i in range(2, int(np.sqrt(N))):
    if N % i == 0:
        N = N // i
        dividers.append(i)

print(dividers)
