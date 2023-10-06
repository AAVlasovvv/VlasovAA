import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

fig = plt.figure(figsize=(10, 7))
ax1 = fig.add_subplot(211)
ax2 = fig.add_subplot(212)

values1 = np.random.normal(0, 100, 500)
values2 = np.random.normal(0, 100, 10000)

ax1.hist(values1, 50)
ax1.grid()

ax2.hist(values2, 100)
ax2.grid()
plt.show()