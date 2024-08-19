# -*- coding: utf-8 -*-
"""
Created on Thu Feb 29 09:56:05 2024

@author: Kaviyarasan PR
"""

""" open GL  - 3D models- mainly on graphics-- GUI """

import matplotlib.pyplot as plt
import numpy as np
x= np.linspace(-5,5,100)
y=x**2
plt.plot(x,y,color="purple", linestyle="--")
 

x1 = np.linspace(-4 * np.pi, 4 * np.pi, 100)
y1 = np.sin(x1)
plt.plot(x1,y1,color="purple", linestyle="--")
"""positional arguments"""

plt.plot(x, y, 'o--', color='red', lw = 2.5, ms = 2)
plt.plot(x, y, 'o--', color='red', lw = 3, ms = 2)

fig, ax= plt.subplots(2, 2, figsize=(4,4))
print(type(fig))
print(type(ax))

xx= ax[0][0]
xx.plot(x,y)


m_fig, m_axes = plt.subplots(2, 2, figsize = (8,4))
ax = m_axes[0][1]
ax.plot(x,y)
ax.set(xlabel='x vlues', ylabel='y values',
        title='Explicit function y = f(x)')
ax = m_axes[1][1]
ax.plot(x1,y1)
ax.set(xlabel='x vlues', ylabel='y values',
        title='Explicit function y = f(x)')
plt.show()





t = np.arange(-100,100, 1)
x = t
y = t ** 2
z = t ** 3

fig = plt.figure()
ax = fig.add_subplot(121, projection='3d')

ax.plot(x, y, z)




x = np.arange(-2.0, 2.0, 0.1)
y = x**2
# The following will print a 3D surface
X,Y=np.meshgrid(x,y) #Forming MeshGrid
Z = X **2 + Y ** 2
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, Z)
ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')
plt.show()

"""contour plot- level set - """