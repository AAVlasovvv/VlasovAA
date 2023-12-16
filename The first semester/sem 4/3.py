import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


df = pd.read_csv("iris_data.csv")
#print(df['Species'])

#Species = df['Species']
Species = list(df['Species'])
PetalLengthCm = list(df['PetalLengthCm'])
Iris_setosa = Species.count('Iris-setosa')
#print(Iris_setosa)    Iris-versicolor     Iris-virginica
Iris_versicolor = Species.count('Iris-versicolor')
Iris_virginica = Species.count('Iris-virginica')
petal_length_less_1dot2 = 0
petal_length_more_1dot2_less_1dot5 = 0
petal_length_more_1dot5 = 0
petal_length_1dot2 = PetalLengthCm.count(1.2)
petal_length_1dot5 = PetalLengthCm.count(1.5)
# print(petal_length_1dot5)
# print(petal_length_1dot2)
for i in range(0,len(PetalLengthCm)):
    if PetalLengthCm[i] < 1.2:
        petal_length_less_1dot2 += 1
    if 1.2 < PetalLengthCm[i] < 1.5:
        petal_length_more_1dot2_less_1dot5 += 1
    if PetalLengthCm[i] > 1.5:
        petal_length_more_1dot5 += 1
# print(petal_length_less_1dot2)
# print(petal_length_more_1dot2_less_1dot5)
# print(petal_length_more_1dot5)

fig = plt.figure(figsize=(20,10))
ax1 = fig.add_subplot(211)
ax2 = fig.add_subplot(212)
#plt.title('Доля видов (Species) ирисов в датасете')
ax1.pie([Iris_setosa, Iris_versicolor, Iris_virginica], autopct='%1.1f%%', labels = ['Iris-setosa','Iris-versicolor','Iris-virginica'])
#ax1.title('Доля видов (Species) ирисов в датасете')
ax1.set_title('Доля видов (Species) ирисов в датасете')
#plt.pie([Iris_setosa, Iris_versicolor, Iris_virginica], autopct='%1.1f%%', labels = ['Iris-setosa','Iris-versicolor','Iris-virginica'])

ax2.pie([petal_length_less_1dot2, petal_length_1dot2, petal_length_more_1dot2_less_1dot5, petal_length_1dot5, petal_length_more_1dot5], autopct='%1.1f%%', labels = ['Меньше 1,2 см','Равно 1,2 см','Больше 1,2 см, но меньше 1,5 см', 'Равно 1,5 см', 'Больше 1,5 см'])
ax2.set_title('Доли ирисов, у которых длина лепестка (PetalLengthCm) больше 1.2см, равно 1.2 см, больше 1.2см и меньше 1.5см, равно 1.5 см, больше 1.5см.')
#plt.title('Доля видов (Species) ирисов в датасете')
fig.show()
plt.show()



