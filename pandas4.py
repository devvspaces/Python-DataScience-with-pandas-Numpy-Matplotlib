#This is another pandas tutorial from PyUniverse, Pandas 4: Descriptive Analysis
import pandas as pd
import numpy as np

#Create a Dictionary of series
d = {'Name':pd.Series(['Tom','James','Ricky','Vin','Steve','Smith','Jack',
   'Lee','David','Gasper','Betina','Andres']),
   'Age':pd.Series([25,26,25,23,30,29,23,34,40,30,51,46]),
   'Rating':pd.Series([4.23,3.24,3.98,2.56,3.20,4.6,3.8,3.78,2.98,4.80,4.10,3.65])}

#Create a DataFrame
df = pd.DataFrame(d)
print(df)

print("Sum")
#Default axis is vertical
print(df.sum())
print(df.sum(axis=1))

print("Count")
print(df.count())

print("Mean,Median,Mode")
print(df.mean())
print(df.median())
print(df.mode())

print("Cummulatives")
print(df.cumsum()["Age"])
print()

print("Descriptive")
print(df.describe())
print(df.describe(include="object"))
print(df.describe(include="all"))