# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 14:29:20 2024

@author: Kaviyarasan PR
"""

""" bracketing-exhaustive search method"""

# def find_minimum(a, b, n, J):
#     # Step 1: Initialize intermediate points
#     delta_w = (b - a) / n
#     w1 = a
#     w2 = w1 + delta_w
#     w3 = w2 + delta_w

#     # Step 2: Check if minimum lies between w1 and w3
#     while J(w1) >= J(w2) <= J(w3):
#         a = w1
#         b = w3
#         delta_w /= n
#         w1 = w2
#         w2 = w3
#         w3 = w2 + delta_w

#     # Step 3: Check if the minimum exists between a and b
#     if J(a) < J(b):
#         return a
#     else:
#         return b

# # Define the function J(w)
# def J(w):
#     return w**2 + (54 / w)

# # Example usage:
# a = 0.1   # Lower boundary
# b = 3.5 # Upper boundary
# n = 10  # Number of intermediate points

# minimum = find_minimum(a, b, n, J)
# print("Minimum value occurs at w =", minimum, "with J(w) =", J(minimum))
"""1 . For the function J(w) = w^2 + (54/w), implement the following methods:
    (a) Use the bracketed value (that you got in the last lab) to get to the critical point employing interval halving method and 
    (b) identify the critical point using Newton-Raphson method and (c) verify the result manually using the optimality criteria
    (post this write-up as well in .jpg/.png etc).

"""

"""interval halving method"""


import matplotlib.pyplot as plt
import numpy as np
a = 1
b = 10
e = 10**-5
wm = (a+b)/2

stop = 1


def J(w):
    return w**2 + (54/w)


while stop:
    L = b-a
    w1 = a + L/4
    w2 = b - L/4

    if J(w1) < J(wm):
        b = wm
        wm = w1
        L = b-a
        if L < e:
            stop = 0
        else:
            w1 = a + L/4
            w2 = b - L/4
    if J(w2) < J(wm):
        a = wm
        wm = w2
        if L < e:
            stop = 0
        else:
            w1 = a + L/4
            w2 = b - L/4
    else:
        a = w1
        b = w2
        L = b-a
        if L < e:
            stop = 0
        else:
            w1 = a + L/4
            w2 = b - L/4


print((wm), J(wm))


x = 5  # initial guess


def f_derivative(x, h=0.01):
    return (J(x + h) - J(x - h)) / (2 * h)


def s_derivative(x, h=0.01):
    return (J(x + h) - 2*J(x) + J(x - h)) / (h**2)


while True:
    x = x - f_derivative(x)/s_derivative(x)
    if abs(f_derivative(x)) < e:
        break

print(x)

"""
2.  Plot the surface J(w1, w2) = (w1 - 10)^2 + (w2 - 10)^2.
 Also, generated the corresponding contour plot. Label the plots appropriately.
 Give a suitable title for the figure.
"""

w1 = np.linspace(-100, 100, 1000)
w2 = np.linspace(-100, 100, 1000)

w1, w2 = np.meshgrid(w1, w2)


def J_values(w1, w2):
    return (w1-10)**2+(w2-10)**2


z = (w1-10)**2 + (w2-10)**2
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(w1, w2, J_values(w1, w2))
ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('J_values(w1,w2)')
ax.set_title('Surface plot of J(w1, w2)')
plt.show()


plt.figure()
contour = plt.contour(w1, w2, z)
plt.clabel(contour)
plt.xlabel("w1")
plt.xlabel("w2")
plt.title("Contour plot")
plt.show()


"""
3. Using line (unidirectional) search, for the function (w1 - 10 )^2 + (w2 - 10)^2, 
find the minimum value along the direction (2, 5). You can assume the start point to be (2,1). 
 Plot the function and its contours along with the minimum value in that direction."""


# import numpy as np
# import matplotlib.pyplot as plt

# # Define the function J(w1, w2)
# def J(w1, w2):
#     return (w1 - 10)**2 + (w2 - 10)**2

# # Define the direction vector
# direction = np.array([2, 5])

# # Define the start point
# start_point = np.array([2, 1])

# # Define the step size for line search
# step_size = 0.1

# # Perform unidirectional line search
# current_point = start_point
# while True:
#     next_point = current_point + step_size * direction
#     if J(*next_point) >= J(*current_point):
#         break
#     current_point = next_point

# minimum_value = J(*current_point)

# # Plot the function and its contours
# w1 = np.linspace(0, 20, 100)
# w2 = np.linspace(0, 20, 100)
# w1, w2 = np.meshgrid(w1, w2)
# J_values = J(w1, w2)

# plt.figure(figsize=(8, 6))
# plt.contour(w1, w2, J_values, levels=20, cmap='viridis')
# plt.plot(current_point[0], current_point[1], 'ro')
# plt.xlabel('w1')
# plt.ylabel('w2')
# plt.title('Contour plot of J(w1, w2) with minimum value along (2, 5)')
# plt.colorbar(label='J(w1, w2)')
# plt.grid(True)
# plt.show()

# print("Minimum value along direction (2, 5):", minimum_value)

def j(a):
    x = 2+a*2
    y = 1+a*5
    return (x - 10)**2 + (y - 10)**2


a = -100
b = 100
n = 2000


def bracket(a, b, n):
    del_w = (b-a)/n
    w1 = a
    w2 = w1+del_w
    w3 = w2+del_w
    while(w3 <= b):
        if j(w1) >= j(w2) <= j(w3):
            flag = 1
            break

        else:
            w1 = w2
            w2 = w3
            w3 = w2 + del_w

    if flag == 1:
        print('minima is between {} and {}'.format(w1, w3))
    else:
        print('minima is either {} or {}'.format(a, b))


bracket(a, b, n)

# print(f" the function value at minima {j(w1)} or {j(w2)}")
