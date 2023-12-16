#МНК для лаб

from statistics import mean
import matplotlib.pyplot as plt

with open("1.2.5.data_1.txt", "r") as fin:
    data = fin.readlines()

I = [float(line.split()[0]) for line in data[1:]]
V = [float(line.split()[1]) for line in data[1:]]


def least_squares(xdata, ydata):
    a = (sum([x * y for x, y in zip(xdata, ydata)]) - mean(ydata) * sum(xdata)) / (sum([x ** 2 for x in xdata]) - mean(xdata) * sum(xdata))
    b = mean(ydata) - a * mean(xdata)
    
    return a, b


print(least_squares(I, V))

a, b = least_squares(I, V)

fig, ax = plt.subplots()
ax.plot(I, V, 'o', label="Данные эксперимента")

xdata = list(range(0, 21))
ax.plot(xdata, [a * x + b for x in xdata], label="Аппроксимация")
ax.set_ylabel("Напряжение, V")
ax.set_xlabel("Сила тока, A")
ax.legend()
#plt.savefig("fig1.png")
plt.show()