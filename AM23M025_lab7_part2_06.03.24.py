# -*- coding: utf-8 -*-
"""
Created on Sat Mar  9 18:30:13 2024

@author: Kaviyarasan PR
"""
"""
5. WAP to plot a 3-d graph of the helical wave signal using the scatter method and normal line method. 
Plot them separately and specify legend.
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Define helical wave function
def helical_wave(t):
    x = np.cos(t)
    y = np.sin(t)
    z = t
    return x, y, z

# Generate data points
t = np.linspace(0, 10*np.pi, 1000)
print(t)
# t= np.arange(0,10*np.pi,1)
# print(t)
x, y, z = helical_wave(t)

# Scatter plot
fig = plt.figure(figsize=(10, 5))

# Normal line plot
ax = fig.add_subplot(122, projection='3d')
ax.plot(x, y, z, c='r', label='Normal Line Method')
ax.set_title('Helical Wave - Normal Line Method')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.legend()

plt.show()

"""

6.

countries = {

    "1": {"Country": "New Country 1",

          "Capital": "New Capital 1",

          "Population": "123,456,789"},

    "2": {"Country": "New Country 2",

          "Capital": "New Capital 2",

          "Population": "987,654,321"},

    "3": {"Country": "New Country 3",

          "Capital": "New Capital 3",

          "Population": "111,222,333"}

}

Make a data frame using pandas from dictionary of dictionary.
"""


countries = {

    1: {"Country": "New Country 1",

          "Capital": "New Capital 1",

          "Population": "123,456,789"},

    2: {"Country": "New Country 2",

          "Capital": "New Capital 2",

          "Population": "987,654,321"},

    3: {"Country": "New Country 3",

          "Capital": "New Capital 3",

          "Population": "111,222,333"}

}

data= pd.DataFrame.from_dict(countries)
print(data)


"""
7.

StringData = ‘’’Date;Event;Cost

    10/2/2011;Music;10000

    11/2/2011;Poetry;12000

    12/2/2011;Theatre;5000

    13/2/2011;Comedy;8000

    ‘’’

Make a data frame using pandas from string.


"""

from io import StringIO

string_data = '''Date;Event;Cost

    10/2/2011;Music;10000

    11/2/2011;Poetry;12000

    12/2/2011;Theatre;5000

    13/2/2011;Comedy;8000

    '''
    
# Convert string to a file-like object
string_io = StringIO(string_data)

# Read the data into a DataFrame, skipping empty lines
df = pd.read_csv(string_io, sep=';', skip_blank_lines=True)

print(df)

"""

8.Take a N X M integer array matrix with space separated elements ( N = rows and M  = columns). 
Your task is to print the transpose and flatten results using numpy
     
"""

matrix= """
1 2 3
4 6 8
2 4 3
"""
    
splitting= np.array([[int(num) for num in row.split()] for row in matrix.strip().split("\n")])
print(splitting)

transpose1= np.transpose(splitting)
print(transpose1)

flat= splitting.flatten()
print(flat)



"""

9. WAP to capitalize a column of names in a Pandas Dataframe.

Eg : Input : {'Name': ['john', 'bODAY', 'aNa', 'Peter', 'nicky'], 'Education': ['masters', 'graduate', 'graduate', 'Masters', 'Graduate'], 'Age': [27, 23, 21, 23, 24]}

Output : {'Name': ['John', 'Boday', 'Ana', 'Peter', 'Nicky'], 'Education': ['masters', 'graduate', 'graduate', 'Masters', 'Graduate'], 'Age': [27, 23, 21, 23, 24]}

"""

dictionary = {
    'Name': ['john', 'bODAY', 'aNa', 'Peter', 'nicky'], 
    'Education': ['masters', 'graduate', 'graduate', 'Masters', 'Graduate'],
    'Age': [27, 23, 21, 23, 24]
    }

df= pd.DataFrame(dictionary)
print(df)

df['Name']=df['Name'].str.capitalize()
print(df)



"""
10. Use the central difference method to find the first and second order derivatives of the function. 
Use the following function for testing the result. And also verify the result manually (Write on paper and upload jpg). 
Refer to section 2.5.1 of “Optimization for Engineering Design: Algorithms and Examples” by KALYANMOY DEB, 2nd edition.


f(x) = 3x**2 + 2x

"""

def f(x):
    return 3*x**2 + 2*x

def f_derivative(x, h=0.01):
    return (f(x + h) - f(x - h)) / (2 * h)

def s_derivative(x, h=0.01):
    return (f(x + h) - 2*f(x) + f(x - h)) / (h**2)

# Testing the derivatives at x = 1
x = 1
first_order = f_derivative(x)
second_order = s_derivative(x)

print("First-order derivative at x =", x, ":", first_order)
print("Second-order derivative at x =", x, ":", second_order)









































