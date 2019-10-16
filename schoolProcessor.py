from school import student
import pandas as pd
df = pd.read_csv("newSchool.csv")
"""
byYears=[]
for i in range(2014,2017):
	get=df.loc[df["Graduated"]==i]
	values=get.groupby("Department").count()["Graduated"]
	byYears+=[list(values)]
d=list(values.index)
year=[2014,2015]
for a,b,c,i in zip(*byYears,d):
	current=[a,b,c]
	print(year,current)
"""
#Those that bear john
for a,b in enumerate(df["Name"].str.contains("John")):
	if b:
		print(df.loc[a])