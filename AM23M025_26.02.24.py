# -*- coding: utf-8 -*-
"""
Created on Mon Feb 26 12:01:31 2024

@author: Kaviyarasan PR
"""

""" if you want to draw a line. First we need to create a new window on the screen"""

""" HW: how to create a window. open and close the window and have a menu on that window"""


import pandas as pd

df = pd.read_csv(r"F:\IITM\Mtech 2_sem\data_science\ED5340_DataScience-main\ED5340_DataScience-main\L13_Libraries\test_data_csv11.csv")
print(df)
print(df['X'])
lst = df['X']
print('Printing the list')
print(lst, type(lst))

for num in lst:
    # print(num, end=" ")
    print(num)
"""seperating the X column alone""" 

df = pd.read_csv(r"F:\IITM\Mtech 2_sem\data_science\ED5340_DataScience-main\ED5340_DataScience-main\L13_Libraries\test_data_csv11.csv", usecols=['X'])
print(df)

"""using the X column as the index of the whole data frame """

df = pd.read_csv(r"F:\IITM\Mtech 2_sem\data_science\ED5340_DataScience-main\ED5340_DataScience-main\L13_Libraries\test_data_csv11.csv", index_col='X')
print(df)

""" what is contigous memory allocation ?"""



import numpy as np

print(np.__version__)


onedarray= np.array([1,2,5,3,5,6,67,234,98235])
print(id(onedarray), id(onedarray[0]))
print(onedarray.itemsize, onedarray.strides)
print(type(onedarray))


arr = np.array([1, 2, 3, 4, 5]) # 

print(id(arr), id(arr[0]))
print(arr.itemsize, arr.strides) #Here the itemsize is a 8 bits (size of one integer). 
print(type(arr))


arr1 = np.array([[1, 2, 3, 4, 5], [1, 2, 3, 4, 5]])

print(id(arr1), id(arr1[0]))
print(arr1.itemsize, arr1.strides)



a = np.array(42)
b = np.array([1, 2, 3, 4, 5])
c = np.array([[1, 2, 3], [4, 5, 6]])
d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])


print(a.ndim, a.shape, a.size, a.dtype, a.itemsize, a.data)
print(b.ndim, b.shape, b.size, b.dtype, b.itemsize, b.data)
print(c.ndim, c.shape, c.size, c.dtype, c.itemsize, c.data)
print(d.ndim, d.shape, d.size, d.dtype, d.itemsize, d.data)


e = np.arange(15)
print(e)

e = np.arange(15).reshape(3,5)
print(e)

x = np.linspace(0, 9, 80)
print(x)


y = np.sin(x)
print(y)


a = np.array(([1, 2], [3, 4]))
b = np.array(([1, 2], [3, 4]))

print(a)
print(b)
print(a * b)  
print(a @ b) 
print(a.dot(b)) 
""" projection of one vector onto the other"""

""" create a normal list. use the operator * to multiply two matrices
     if the two matrices have different order how will the element wise multiplication work"""

""" * here is the broadcasting operator. That is an element wise multiplication """