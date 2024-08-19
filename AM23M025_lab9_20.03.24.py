# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 14:10:18 2024

@author: Kaviyarasan PR
"""

"""
1. For the question in last week's lab, is the search direction a gradient descent one? Comment on that.

"""

"""

2.Using steepest gradient descent, find all the local minima for the function  J(x1, x2) = (x1^2+x2−11)^2+(x1+x2^2−7)^2. 
While applying gradient descent, do the following (a) Fixing the value for alpha (b) use line search to determine the value for alpha.
 Plot the intermediate steps in the iteration to show one of the minimal point.

"""

import numpy as np
import matplotlib.pyplot as plt

def J(x1, x2):
    return (x1**2 + x2 - 11)**2 + (x2**2 + x1 - 7)**2

x1 = np.linspace(-4, 4, 100)
x2 = np.linspace(-4, 4, 100)

X1, X2 = np.meshgrid(x1, x2)  # Create meshgrid

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X1, X2, J(X1, X2))
ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('J_values(x1,x2)')
ax.set_title('Surface plot of J(x1, x2)')
plt.show()


# Define the gradient function using numerical differentiation
def gradient_J(x1, x2, h=1e-5):
    grad_x1 = (J(x1 + h, x2) - J(x1, x2)) / h
    grad_x2 = (J(x1, x2 + h) - J(x1, x2)) / h
    return np.array([grad_x1, grad_x2])

def line_search(x, direction, func=J, a=0.01, b=1.0, tol=1e-4):
  """Line search using interval halving"""
  while b - a > tol:
    mid = (a + b) / 2
    if func(*(x + mid * direction)) < func(*x):  # Unpack x and direction
      b = mid
    else:
      a = mid
  return (a + b) / 2  # Average of final interval

# Define the gradient descent algorithm
def gradient_descent(starting_points, learning_rate=0.01, max_iterations=20, tolerance=1e-6):
    trajectories = []
    minima_points = []
    for start_point in starting_points:
        x1, x2 = start_point
        iteration = 0
        trajectory = [(x1, x2)]     
    
        while iteration < max_iterations:
            # Compute gradient
            grad = gradient_J(x1, x2)
        
            # Update parameters
            x1 -= learning_rate * grad[0]
            x2 -= learning_rate * grad[1]
        
            trajectory.append((x1, x2))
        
            # Check for stopping criteria
            if np.linalg.norm(grad) < tolerance:
                break
        
            iteration += 1
            
            alpha = line_search(np.array([x1, x2]), grad)
            print(alpha)
    
        trajectories.append(trajectory)
        minima_points.append((x1, x2))
    
    return trajectories, minima_points

# Define starting points for gradient descent
starting_points = [(-3, 2), (-2, -1), (0, 3), (2, -2), (3, 3), (0, 0)]

# Perform gradient descent
trajectories, minima_points = gradient_descent(starting_points)

for i, point in enumerate(minima_points):
    print("Finding minimum Using Gradient Descent")
    print(f"Starting Point {starting_points[0+i]}: Final Minimum Point: ({point[0]:.2f}, {point[1]:.2f})")


plt.figure()
contour = plt.contour(X1, X2, J(X1, X2), levels=100)
plt.clabel(contour)
plt.xlabel("w1")
plt.ylabel("w2")
plt.title("Contour plot")

# Plot trajectories on the contour plot
for trajectory in trajectories:
    x1_values = [point[0] for point in trajectory]
    x2_values = [point[1] for point in trajectory]
    plt.plot(x1_values, x2_values, marker='o')

plt.show()




# import numpy as np
# import matplotlib.pyplot as plt
# def J(x1,x2):
#     return (x1**2 + x2 - 11)**2 + (x2**2 + x1 - 7)**2

# x1= np.linspace(-4,4,100)
# x2= np.linspace(-4,4,100)

# # x1,x2= np.meshgrid(x1,x2)

# # fig = plt.figure()
# # ax = fig.add_subplot(111, projection='3d')
# # ax.plot_surface(x1, x2, J(x1, x2))
# # ax.set_xlabel('X Label')
# # ax.set_ylabel('Y Label')
# # ax.set_zlabel('J_values(x1,x2)')
# # ax.set_title('Surface plot of J(x1, x2)')
# # plt.show()

# # plt.figure()
# # contour = plt.contour(x1,x2,J(x1,x2), levels=100)
# # plt.clabel(contour)
# # plt.xlabel("w1")
# # plt.xlabel("w2")
# # plt.title("Contour plot")
# # plt.show()




# # Define the gradient function using numerical differentiation
# def gradient_J(x1, x2, h=1e-5):
#     grad_x1 = (J(x1 + h, x2) - J(x1, x2)) / h
#     grad_x2 = (J(x1, x2 + h) - J(x1, x2)) / h
#     return np.array([grad_x1, grad_x2])

# # Define the gradient descent algorithm
# def gradient_descent(learning_rate=0.01, max_iterations=16, tolerance=1e-6):
#     # Starting point
#     x1 = 0
#     x2 = 0
#     iteration = 0
#     trajectory = [(x1, x2)]     
    
#     while iteration < max_iterations:
#         # Compute gradient
#         grad = gradient_J(x1, x2)
        
#         # Update parameters
#         x1 -= learning_rate * grad[0]
#         x2 -= learning_rate * grad[1]
        
#         trajectory.append((x1, x2))
#         # Check for stopping criteria
#         if np.linalg.norm(grad) < tolerance:
#             break
        
#         iteration += 1
    
#     return x1, x2, J(x1, x2),trajectory
    

# # Perform gradient descent
# opt_x1, opt_x2, min_J, trajectory = gradient_descent()

# print("Optimal values:")
# print("x1:", round(opt_x1))
# print("x2:", round(opt_x2))
# print("Minimum value of J:", (min_J))

# plt.figure()
# contour = plt.contour(x1, x2, J(x1,x2), levels=100)
# plt.clabel(contour)
# plt.xlabel("w1")
# plt.ylabel("w2")
# plt.title("Contour plot")

# # Perform gradient descent
# trajectory = gradient_descent()

# # Extract x1 and x2 coordinates from the trajectory
# x1_values = [point[0] for point in trajectory]
# x2_values = [point[1] for point in trajectory]

# # Plot the trajectory on the contour plot
# plt.plot(x1_values, x2_values, marker='o', color='red')

# plt.show()




# import numpy as np
# import matplotlib.pyplot as plt

# def J(x1, x2):
#     return (x1**2 + x2 - 11)**2 + (x2**2 + x1 - 7)**2

# x1 = np.linspace(-4, 4, 100)
# x2 = np.linspace(-4, 4, 100)

# X1, X2 = np.meshgrid(x1, x2)  # Create meshgrid

# # Define the gradient function using numerical differentiation
# def gradient_J(x1, x2, h=1e-5):
#     grad_x1 = (J(x1 + h, x2) - J(x1, x2)) / h
#     grad_x2 = (J(x1, x2 + h) - J(x1, x2)) / h
#     return np.array([grad_x1, grad_x2])

# # Define the gradient descent algorithm
# def gradient_descent(learning_rate=0.01, max_iterations=100, tolerance=1e-6):
#     # Starting point
#     x1 = -3
#     x2 = 2
#     iteration = 0
#     trajectory = [(x1, x2)]     
    
#     while iteration < max_iterations:
#         # Compute gradient
#         grad = gradient_J(x1, x2)
        
#         # Update parameters
#         x1 -= learning_rate * grad[0]
#         x2 -= learning_rate * grad[1]
        
#         trajectory.append((x1, x2))
        
#         # Check for stopping criteria
#         if np.linalg.norm(grad) < tolerance:
#             break
        
#         iteration += 1
    
#     # Return trajectory alongside other values
#     return x1, x2, J(x1, x2), trajectory

# # Perform gradient descent
# opt_x1, opt_x2, min_J, trajectory = gradient_descent()

# print("Optimal values:")
# print("x1:", round(opt_x1))
# print("x2:", round(opt_x2))
# print("Minimum value of J:", min_J)

# plt.figure()
# contour = plt.contour(X1, X2, J(X1, X2), levels=100)  # Use meshgrid X1, X2
# plt.clabel(contour)
# plt.xlabel("w1")
# plt.ylabel("w2")
# plt.title("Contour plot")

# # Extract x1 and x2 coordinates from the trajectory
# x1_values = [point[0] for point in trajectory]
# x2_values = [point[1] for point in trajectory]

# # Plot the trajectory on the contour plot
# plt.plot(x1_values, x2_values, marker='o', color='red')

# plt.show()








