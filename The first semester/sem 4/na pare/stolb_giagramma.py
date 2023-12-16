import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# принцип настройки схожий, но вместо plt.plot используем plt.bar
labels = ['A', 'B', 'C']
values = [5,8,2]

plt.figure(figsize=(8,4), dpi=100)

bars = plt.bar(labels, values)

#plt.savefig('barchart.png', dpi=300)

plt.show()