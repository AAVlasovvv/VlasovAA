import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv("BTC_data.csv")
Timedurty = list(df['time'])
Close = list(df['close'])
Time = []
for i in range(len(Timedurty)):
    Time.append(Timedurty[i][8:10] + Timedurty[i][4:8] + Timedurty[i][2:4])
# print(Timedurty)
# print(Time)

x = np.array(Time)
y = np.array(Close)

plt.figure(figsize=(15,8), dpi=100)
plt.plot(x, y, 'g', label='Price BTC')
plt.xticks(Time[::150])
plt.title('Ты родился слишком поздно, чтобы ...', fontdict={'fontname': 'sans-serif', 'fontsize': 20})

plt.grid()

plt.legend()

plt.show()



