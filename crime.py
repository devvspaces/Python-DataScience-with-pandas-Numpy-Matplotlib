import pandas as pd
import os
#from matplot&lib import pyplot as plt
os.chdir("/storage/emulated/0/Python codes path/Data science")
df = pd.read_csv("crime.csv")
df["TimeS"]=pd.to_datetime(df["cdatetime"])
ts=pd.TimeStamp("1/2/2006")
print(ts)