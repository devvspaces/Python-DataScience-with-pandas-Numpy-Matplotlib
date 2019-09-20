#Basic funtionality for Pandas
#works for Series/Dataframes
import pandas as pd
d = {'Name':pd.Series(['Tom','James','Ricky','Vin','Steve','Smith','Jack']), 'Age':pd.Series([25,26,25,23,30,29,23]),'Rating':pd.Series([4.23,3.24,3.98,2.7,5.3,2.4,3.2])}
d=pd.DataFrame(d)
print(d)
#Data axes
print(d.axes)
#... dtypes, returns types of each columns
print(d.dtypes)
#...empty, Returns true is dataframe is empty
print(d.empty)
#...ndim, obviously 2D
print(d.ndim)
#...size, returns the amounts of items
print(d.size)
#...values, returns an ndarray type of data
print(d.values)
#...T(ranspose), turns index to columns and columns to index
print(d.T)
#...head(),tail()
print(d.head(),d.tail(3))

#Descriptive Analysis
#Sum, returns concatenation of strings and sums of numbers, default axis is 0
print(d.sum())