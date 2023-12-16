#МНК для лаб сделанное на уровне эксперт

import numpy as np
import matplotlib.pyplot as plt

with open("1.2.5.data_1.txt", "r") as fin:
    data = fin.readlines()

I = [float(line.split()[0]) for line in data[1:]]
V = [float(line.split()[1]) for line in data[1:]]

x = np.array(I)
y = np.array(V)

A = np.vstack([x, np.ones(len(x))]).T
m, c = np.linalg.lstsq(A, y, rcond=None)[0]
plt.plot(x, y, 'o', label='Данные', markersize=6)
plt.plot(x, m * x + c, 'r', label='Аппроксимация')
plt.legend()
plt.show()
