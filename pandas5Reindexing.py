#Pandas 5. Reindexing
import pandas as pd
import numpy as np

N=20

df = pd.DataFrame({
   'A': pd.date_range(start='2016-01-01',periods=N,freq='D'),
   'x': np.linspace(0,stop=N-1,num=N),
   'y': np.random.rand(N),
   'C': np.random.choice(['Low','Medium','High'],N).tolist(),
   'D': np.random.normal(100, 10, size=(N)).tolist()
})
print(df)
#reindex the DataFrame
df_reindexed = df.reindex(index=[0,2,5], columns=['A', 'C', 'B'])

print(df_reindexed)

print("#Reindexing with likes")
df1 = pd.DataFrame(np.random.randn(6,3),columns=['col1','col2','col3'])
df2 = pd.DataFrame(np.random.randn(2,3),columns=['col1','col2','col'])
#Where the columns does not match it fills it up with NaN values
print(df1.reindex_like(df2))
print("NaNs")
#Reindexing with fill nan
df2 = pd.DataFrame(np.random.randn(10,3),columns=['col1','col2','col3'])
print(df1.reindex_like(df2,method="ffill"))
#Setting fill limit
print(df1.reindex_like(df2,method="ffill",limit=1))

print("#Reindexing by modifying column and index names")
new_c=["a","b","c"]
new_i=list("carpet")
c_d={k:v for k,v in zip(df1.columns,new_c)}
print(c_d)
i_d={k:v for k,v in zip(df1.index,new_i)}
print(i_d)
print(df1.rename(columns=c_d,index=i_d))