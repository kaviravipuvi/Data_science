# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 14:14:37 2024

@author: Kaviyarasan PR

"""



"""1. Write a program that takes coefficients A, B, C, D, and E as inputs representing a 4th degree polynomial in the form
 Ax^4 + Bx^3 + Cx^2 + Dx + E. Calculate the values of this polynomial for x in the range from -100 to 100,
 with constant discrete intervals.

Store the resulting x and y values as a NumPy array, where x represents the input values, and y represents the corresponding output values
 of the polynomial. Finally, use Matplotlib to plot the graph using the generated NumPy array.

"""
import numpy as np
import matplotlib.pyplot as plt


def polynomial(A,B,C,D,E,x):
    return A*x**4+ B*x**3 + C*x**2 + D*x + E

A= int(input("enter the coeff:"))
B= int(input("enter the coeff:"))
C= int(input("enter the coeff:"))
D= int(input("enter the coeff:"))
E=int(input("enter the coeff:"))


x_range= np.arange(-100,101,1)
print(x_range)

y_values = np.zeros(len(x_range))

for i,x in enumerate(x_range):
    # print(x)
    y_values[i]=polynomial(A,B,C,D,E, x)


plt.plot(x_range, y_values)
plt.title('polynomial plot')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.grid(True)
plt.show()

"""
2. Suppose you have a dictionary containing information about monthly sales for different products over a period of time. 
The dictionary has the following structure.

sales_data = {

    'Product': ['A', 'B', 'A', 'C', 'B', 'C', 'A', 'B', 'C'],

    'Month': ['Jan', 'Jan', 'Feb', 'Feb', 'Mar', 'Mar', 'Apr', 'Apr', 'Apr'],

    'Sales': [100, 150, 200, 120, 180, 220, 90, 110, 130]

}

Write a Python script to convert this dictionary into a pandas DataFrame, 
calculate the total sales for each product over the entire period, and then create a bar plot using
 matplotlib to visualize the total sales for each product.
"""

import pandas as pd
import matplotlib.pyplot as plt

sales_data = {

    'Product': ['A', 'B', 'A', 'C', 'B', 'C', 'A', 'B', 'C'],

    'Month': ['Jan', 'Jan', 'Feb', 'Feb', 'Mar', 'Mar', 'Apr', 'Apr', 'Apr'],

    'Sales': [100, 150, 200, 120, 180, 220, 90, 110, 130]

}


df= pd.DataFrame(sales_data)

# Group by 'Month' and 'Product' and sum the 'Sales'
monthly_sales = df.groupby(['Month', 'Product']).sum()

summ= df.groupby('Product')['Sales'].sum()
print(summ)

order = ['Jan', 'Feb', 'Mar', 'Apr']
monthly_sales = monthly_sales.reindex(order, level=0)
print(monthly_sales)

summ.plot(kind='bar')
monthly_sales.plot(kind='bar', stacked= False)
plt.title('Monthly Sales by Product')
plt.xlabel('Month')
plt.ylabel('Sales')
plt.legend(title='Product')
plt.show()


"""

3. Create visualizations for the following mathematical functions using Matplotlib:

Plot the following single-variable functions over the range 

[−10,10], and include a title and labels for the axes:

(1) y = cos(x)

(2) y = e^x

(3) y = log(x), where x>0


Generate surface plots for these multi-variable functions over the range 

x=[−10,10] and y=[−10,10] , ensuring to add a title and labels for all axes:

(1) z = cos(sqrt(x^2+y^2)

(2) z = e^(-(x^2+y^2))

(3) z =  log(x^2+y^2) where x^2+y^2>0

"""

x=np.arange(-10,11,0.1)
y=np.cos(x)
plt.plot(x,y, color='red')
plt.title("cos function")
plt.ylabel("f(x)= cos(x)")
plt.xlabel("x")

x=np.arange(-10,11,0.1)
y=np.exp(x)
plt.plot(x,y, color='blue')
plt.title("exponential function")
plt.ylabel("f(x)= e^x")
plt.xlabel("x")



x=np.arange(0,11,0.1)
y=np.log(x)
plt.plot(x,y, color='yellow')
plt.title("log function")
plt.ylabel("f(x)= log(x) ")
plt.xlabel("x")

x=np.arange(-10,11,0.1)
y=np.arange(-10,11,0.1)
x,y=np.meshgrid(x,y)
z=np.cos(np.sqrt(x**2+y**2))
plt.figure()
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(x,y,z)

ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Cos function ')
plt.show()

x=np.arange(-10,11,0.1)
y=np.arange(-10,11,0.1)
x,y=np.meshgrid(x,y)
z = np.exp(-(x**2+y**2))
plt.figure()
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(x,y,z)
ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Exponential function ')


x=np.arange(0,11,0.1)
y=np.arange(0,11,0.1)
x,y=np.meshgrid(x,y)
z = np.log(x**2+y**2)
plt.figure()
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(x,y,z)
ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('log function')






"""
4. For the function J(w) = w^2 + (54/w), implement the bracketing method (choose your own a, b, n).

"""       
# def function(w):
#     return w**2 + (54/w)

# def find_minimum(a, b, n):
#     # Step 1: Calculate the step size
#     delta_w = (b - a) / n
    
#     # Initial points
#     w1 = a
#     w2 = w1 + delta_w
#     w3 = w2 + delta_w
    
#     # Loop through intervals
#     while w3 <= b:
#         # Calculate function values at interval endpoints
#         f1 = function(w1)
#         f2 = function(w2)
#         f3 = function(w3)
        
#         # Check if the minimum lies within the current interval
#         if f2 < f1 and f2 < f3:
#             print(f"Local minimum lies between {w1} and {w3}")
#             return
        
#         # Move to the next interval
#         w1 = w2
#         w2 = w3
#         w3 += delta_w
    
#     # If no minimum found within the interval
#     print("No local minimum exists within the interval.")
    
#     print(min(a,b))

# # Input values
# a = 0.1
# b = 0.2
# n = 10

# # Find the minimum
# find_minimum(a, b, n)

'''4. For the function J(w) = w^2 + (54/w), implement the bracketing method
 (choose your own a, b, n).'''
import numpy as np
import matplotlib.pyplot as plt

w=np.linspace(-10,10+1,1000)
J=w**2+54/w
plt.plot(w,J)


a=-10;  b=10;    n=20
del_w=(b-a)/n

w1=a
w2=w1+del_w
w3=w2+del_w
#res1=0;res2= 0;res3=0;res4=0

flag=0
w=np.linspace(a,b,n+1)
'''no need b+1'''
J=w**2+54/w

j={}
for a,b in zip(w,J):
    #print(a,b)
    j[int(a)]=b
    

print(w1,w2,w3,j[w1],j[w2],j[w3])
while(w3<=b):
    if j[w1]<j[w2]<j[w3]:
        
        res1=w1
        res2= w2
        res3=j[w1]
        res4=j[w2]
        # res3=j[round(w1)]
        # res4=j[round(w2)]
        flag=1
        break
    
    else:
       # print(w1,w2,w3,j[round(w1)],j[round(w2)],j[round(w3)])
        w1 = w2
        w2 = w3
        w3 = w2 + del_w
    if w3>b:
        flag=0
 
if flag==1:
    print(f'minimum value is in between {res3} and  {res4} and minima occurs in {w1}<=w<={w2}')   
else:
    z=min(a,b)
    print(f'minimum value is may be {z} but  minima doesnt  occur in {a}<w<{b}')

