#DataScienceTutorial2: DataFrames
#ProgrammingUniverse
"""DataFrames can be created in different ways
* List of lists
* List of dicts
* Dict of series
* Dict of list or ndarray
Dataframe structure
pandas.DataFrame(data, index, columns, dtype)
Pandas is great, it can contain different datatypes, it handles missing data correctly
"""
import pandas as pd
import numpy as np
print("#Creating Empty dataframe")
df=pd.DataFrame()
print(df,"\n")

print("#Creating dataframe with lists")
data=[34,63,73,43,98,56,89]
print("#Index and columns default is range(length of data) and rank respectively")
df=pd.DataFrame(data)
print(df,"\n")
df=pd.DataFrame(data,index=["a","b","c","d","e","f","g"], dtype="float")
print(df,"\n")

print("#Creating with List of lists")
data=[["a",3],["b",5],["c",8]]
df= pd.DataFrame(data,columns=["Letter","No."])
print(df,"\n")

print("#Creating with list of dicts")
data=[{"Name":"Ayo", "Age":18},{"Name":"Holand","Age":21,"Weight/Lbs":30}]
df=pd.DataFrame(data)
print(df,"\n")
#^^^Notice Weight is not in first dict, so pandas considers it as NaN instead of spoiling the dataframe
#We can call colums for list of dics too
df=pd.DataFrame(data,columns=["Name","0Names"])
print("#Notice names is not in data dict as key, so all it's values will be NaN")
print(df,"\n")

print("#Create from dict of lists or ndarray")
data={"Name":["Jake","Sam","Sandra","Corey","Netrobe"],"Age":np.arange(17,22),}
df = pd.DataFrame(data, index=["rank 1","rank 2","rank 3","rank 4","rank 5"])
print(df,"\n")

print("#Creating with dict of series")
data={"Name":pd.Series(["Jake","Sam","Sandra","Corey","Netrobe"], index=[1,2,3,4,5]),"Age":pd.Series(np.arange(17,21), index=[1,2,3,4])}
df=pd.DataFrame(data)
print(df,"\n")
print("Addition/Deletion/Selection/Slicing")
print("Addition")
#I will be using the above data to work
print("Selecting by Label(Column Name)")
print(df["Name"])
print("Add new column")
df["Join"] = pd.Series(np.arange(4), index=[1,2,4,5])
print("New DataFrame","\n",df)
print("Performing Mathematical Operation with columns")
df["add"]=df["Age"]+df["Join"]
#Scalar operate with data
df["multiply"] = df["Join"] * 2
df["Division"] = df["multiply"] / df["add"]
print("New DataFrame","\n",df)
print("Deleting from a dataframe")
del df["Name"]
df.pop("Division")
print("New DF","\n",df,"\n")
print("Selection by locating Label and Integer Location")
print(df.loc[3])
#Doesn't matter if index is not a number if index of row is 'b' you use df.loc['b']'
print(df.iloc[2])
#Counts integers by index even if you don't have numbered indexes'
print(df[1:3])
print("Appending two dataframes")

data={"Name":pd.Series([2,5,6,7,9], index=[1,2,3,4,5]),"Age":pd.Series(np.arange(17,21), index=[1,2,3,4])}
df1=pd.DataFrame(data)

df2= pd.DataFrame({"Name":pd.Series([32,12,23,9,61], index=[1,2,3,4,5]),"Age":pd.Series(np.arange(17,21), index=[1,2,3,4])})

new_df=df1.append(df2)
print(new_df)

print("Dropping a dataframe")
new_df=new_df.drop(1)
#Drops all index of value 1 then assigns new value to variable
print(new_df)

#This is a new tutorial on DataFrame for pandas, i recommend you play with the codes by yourself, get errors and understand it better.
#HappyCoding