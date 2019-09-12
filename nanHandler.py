import pandas as pd

#I used the parse dates to convert my column of dates like to real pandas datesTimeStamp
df = pd.read_csv("Missing.csv", parse_dates=["Year"])

#I then used the converted dates as index, inplace must be = True
df.set_index("Year", inplace=True)
print(df)

#Filled all NaN values with 0, irrespective of the column, you can use 1 or 2,3,4 but i used 0
new_df=df.fillna(0)
print(new_df)

#For specific columns
new_df=df.fillna({"Morning":0, "Night":0})
print(new_df)

#Carry forward previous value to NaNs, visualize like it is moving non NaN values down
new_df=df.fillna(method="ffill")
#Notice in your output for this statement that the first NaN value did not change
print(new_df)#see below

#Carry backward previous value to NaNs, visualize like it is carrying the previous value up
new_df=df.fillna(method='bfill')
#Notice top nan is gone, the method you use depends on how you want to evaluate your missing data
print(new_df)
#You can add limits and axis for the methods too
#Limit means at most, so limit=1 means at most move once
print(df.fillna(method='bfill', limit=1))
#Axis=columns changes nan by moving backwards horizontally towards the left when used with bfill method
print(df.fillna(method='bfill', axis="columns"))

#What if we want the NaN to look real, we can't have totally equal values in the NaN
print(df.interpolate())#This here finds for the average value a NaN value can be equal to by using the nearest top and botton value
print(df.interpolate(method="time"))#This is like above but it also calculates the NaN values for the missing days, making NaN more reasonable, ***Displays values for given index only

#Dropping NaN rows
print(df.dropna())#Automatically drops all rows that contains NaN
print(df.dropna(thresh=1))#Removes rows that has more than one NaN value

#Little time function with pandas
dt=pd.date_range("01-01-2019","01-10-2019")
idx=pd.DatetimeIndex(dt)
df=df.reindex(idx)
print(df)

#Now let do a full good cleaning for our complete indexed data
#From our experience with data cleaning, we saw that interpolate method with time will be the best for this data
#So
df = df.interpolate(method="time")
print(df)
#From our output, we saw that the two first values for the night column is not cleaned, because it only has nearest lower but not nearest upper.
#We will have to use bfill to clean it
df = df.fillna(method="bfill")
#Your result may be different depending on the output you want to get without dropping any rows
print(df)
#Play around with the code and solve the exercise any way you want without deleting any row
#Post Your code and output, i will review it
#Programming Universe Cares