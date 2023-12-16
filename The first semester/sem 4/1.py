import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

with open("exp.txt", "r") as fin:
    data = fin.readlines()

I = [float(line.split()[0]) for line in data[1:]]
V = [float(line.split()[1]) for line in data[1:]]

x = np.array(I)
y = np.array(V)

plt.figure(figsize=(8,5), dpi=100)
plt.plot(x, y, 'g')

plt.title('Соотношение силы тока и напряжения', fontdict={'fontname': 'sans-serif', 'fontsize': 20})

plt.xlabel('Сила тока, I')
plt.ylabel('Напряжение, V')
plt.grid()
plt.legend()
plt.show()