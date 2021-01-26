import pandas as pd
import numpy as np
import matplotlib.pyplot as plt



df = pd.read_csv('titanic.csv')

#Q1
print(df[df['Survived'] == 1][['Pclass', 'Name']])

#Q2
df['Age'].fillna(df['Age'].mean(), inplace=True)

#Q3
print(df.groupby(['Pclass']).size())

#Q4
plt.hist(df['Age'])
plt.show()

