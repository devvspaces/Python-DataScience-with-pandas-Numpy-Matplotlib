import pandas as pd
import os
from matplotlib import pyplot as plt
os.chdir("/storage/emulated/0/Python codes path/Data science")
df = pd.read_csv("crime.csv")
df["TimeS"]=pd.to_datetime(df["cdatetime"])
df["Day"]=df["TimeS"].dt.day
vas=df["Day"].value_counts().sort_index()
y=list(vas)
x=list(vas.index)

plt.bar(x,y,color=["r","g","b","y"],label="Crimes rate per month")
plt.xlabel("Months")
plt.ylabel("Crime rates")
plt.legend()
plt.show()