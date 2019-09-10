import pandas as pd
import numpy as np
#Empty Series
s=pd.Series()
print("Empty Series","\n",s,type(s),"\n")

array=np.array([1,2,3,5])

#Without index
s=pd.Series(array,dtype="float")
print(s,"\n")

#With index
s=pd.Series(array,np.arange(2,6))
print(s,"\n")

#dictionary With too much indexes
array={"a":3,"b":7,"c":8}
s=pd.Series(array,np.array(["a","d","b","c"]))
print(s,"\n")

#Creating Series from scalar
s=pd.Series(5,np.arange(10), dtype="int")
print(s,"\n")

#Picking and Slicing series
arr= np.arange(1,10)
s = pd.Series(arr,dtype="float")
print(s)
#first element
print(s[0])
#first four elements
print(s[:5])
#last four elements
print(s[-4:])
#reverse elements
print(s[::-1])