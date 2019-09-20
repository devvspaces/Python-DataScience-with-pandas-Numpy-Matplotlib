import pandas as pd
d1=[30,36,23,26,34,56,34,10]
d2=["20190801","20190803","20190805","20190807","20190808","20190810","20190812","20190814"]
df = pd.DataFrame({"Date":d2,"Data":d1})
df["Time"]=pd.to_datetime(df["Date"])
date=pd.to_datetime("08/07/2019")
print(date)
x=df["Time"].max()
y=df["Time"].min()
print(x,y)
print(x-y)