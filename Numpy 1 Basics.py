#Pyuniverse here again
#Datascience Numpy 1:Basics
#Free lectures on datascience for pandas,numpy and matplotlib ongoing visit www.fb.me/pyuniverse

#Creating a numpy array is as simple as below
import numpy as np
print(np.zeros((2,5),dtype="int"))#Zeros
print("\n")
print(np.ones((2,3)))#ones
#default dtype is float
print("\n")
print(np.eye(2,2))#like identity matrix
print("\n")
print(np.full((2,3),5))#full of 5
print("\n")
print(np.arange(0,20,2).reshape(2,5))#range from zero to 19 with step of 2
print("\n")
print(np.linspace(2,6,10))#returns 5 elements from 2 to 6
print("\n")

#You can perform scalar and ndarry to ndarray operation,+,-,/,*,**,//,%
data1=np.arange(20).reshape(4,5)
data2=np.linspace(-1,5,20).reshape(4,5)
data3=np.arange(20).reshape(2,2,5)
#We can add two ndarray of the same shape
print(data1+data2)
print("\n")
#But this won't evaluate so i am using try except
try:
	print(data1+data3)
except:
	print("Broadcasting error")
	pass
print("\n")
#Scalar with ndarray
print(data1/2)
print("\n")
#Numpy has it own universal function like...
print(np.max(data1))
print(np.sum(data3))
print("\n")
#Slicing: this is different per the dimension of the nd array
def f(x,y,z):
	return 10*x+y+z
a=np.fromfunction(f,(2,2,4),dtype="int")#Creates a 3dimensional ndarray: two 2d ndarray
#NOTE: 1D MEANS 1 DIMENSION , JUST AN NDARRAY
print(a)
print(a[:,:,0:2])#returns all 2d arrays, all 1d arrays and first to second element in them
print("\n")
a=a.ravel().reshape(4,4)#converts array to that one dimension then reshapes it to 2 dimension
print(a)
print(a[2,:])#third 1d array and all elements in them
#Its just like list butbmore than lists
#Please ensure you play with the codes, practice them and read more on all the infos i gave
#Happy coding guys all love from Programming universe