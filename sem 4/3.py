import pandas as pd
#import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("iris_data.csv")
print(df)
# Printing top 5 rows
df.head()
c = df.shape
print(c[0])
flowers = []

#for  i in range (c[0]):
