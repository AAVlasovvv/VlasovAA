import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

fig = plt.figure(figsize=(10, 7))  # создали рисунок/Figure Fig пропорциями 16:9
ax1 = fig.add_subplot(
    211)  # создали Axes (подграфик) ax1 в серии из 2 графиков, поставили на позицию [1,1] -- левый верхний угол
ax2 = fig.add_subplot(
    212)  # создали Axes ax2 в серии из 2 графиков, поставили на позицию [1,2] -- первый график во второй "строке" графиков

# сгенерируем данные для какой-нибудь гистограммы
values1 = np.random.normal(0, 100, 500)
values2 = np.random.normal(0, 100, 10000)
# строим гистограмму с 50 блоками
ax1.hist(values1, 50)
ax1.grid()  # делаем сетку на графике ax1

ax2.hist(values2, 100)
ax2.grid()  # делаем сетку на графике ax1
plt.show()