#Iterating in pandas #6
import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randn(4,3),columns = ['col1','col2','col3'])

#Returns only column key
for i in df:
	print(i)

#Iteritems:iterates through each column and returns values with tgeir key
for i,v in df.iteritems():
	print(i,v,type(v))
	#Key and series each

#iterrows iterates across each row
for i,v in df.iterrows():
	print(i,v,type(v))
	#Index and Series each

#itertuples, iterates to return a tuple
for i in df.itertuples():
	print(i,type(i),i[0])
	#returns a tuple of type pandas which you can select from or slice