# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 14:21:57 2024

@author: Kaviyarasan PR
"""

"""
1) Implement the generalized equation for finding the gradient of m-samples, each having n-features. 
Also, implement the gradient descent approach assuming a constant learning rate.

2) Using the code developed for problem 1, do the linear regression for the univariate problem using the attached data
 file univariate_linear_regression.csv. Plot the cost function (both as surface as well as contour) 
 as well as the best fit line. 

3) Using the code developed for problem 1, do the linear regression for the multivariate 
problem using the attached data file heart.data.csv. Plot the best fit plane for the given data. 
Can you also interpret the result (taking one independent variable at a time)?

"""

import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt

def gen_equ_gd(x,y):
    col= np.ones(x.shape[0])
    data= np.insert(x,0,col, axis=1)
    w= np.random.randn(data.shape[1])
    gradj=np.zeros(len(w))
    loss_var=[]
    for i in range(1000):
        h= data@w
        loss= (np.sum((h-y)**2))/(2*data.shape[1])
        loss_var.append(loss)
        for j in range(len(gradj)):
            gradj[j]= np.dot((h-y),data[:,j])/data.shape[0]
        w-=(0.01*gradj)
    return loss_var, w

# print(w)

data = pd.read_csv(r"F:\IITM\Mtech 2_sem\data_science\lab_py_files\univariate_linear_regression.csv")

# Assuming the CSV has columns 'x' and 'y', and you want to use them for regression
x = data['x'].values.reshape(-1, 1)  # Reshape to make it a column vector
y = data['y'].values

# Call the function with loaded data
# print(gen_equ_gd(x, y))
loss_var,w = gen_equ_gd(x, y)
plt.plot(loss_var)
plt.title('Loss Function over Iterations')
plt.xlabel('Iteration')
plt.ylabel('Loss')
plt.show()

# Plot the best fit line
plt.scatter(x, y, label='Data')
plt.plot(x, np.dot(np.insert(x, 0, np.ones(x.shape[0]), axis=1), w), color='red', label='Best Fit Line')
plt.title('Best Fit Line')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()

# Plot the loss function as a surface
fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111, projection='3d')
w0_vals = np.linspace(-20 ,20, 1000)
w1_vals = np.linspace(-20, 20, 1000)
w0, w1 = np.meshgrid(w0_vals, w1_vals)
# print(w0)
# print(w1)
J_vals = np.zeros_like(w0)
for i in range(len(w0_vals)):
    for j in range(len(w1_vals)):
        J_vals[i, j] = np.sum((x * w0[i, j] + w1[i, j] - y) ** 2) / (2 * x.shape[0])
ax.plot_surface(w0, w1, J_vals, cmap='viridis')
ax.set_xlabel('w0')
ax.set_ylabel('w1')
ax.set_zlabel('Loss')
ax.set_title('Loss Function Surface')
plt.show()

# Plot the loss function as a contour
plt.figure(figsize=(10, 6))
plt.contour(w1, w0, J_vals, levels= 100)
plt.xlabel('w0')
plt.ylabel('w1')
plt.title('Loss Function Contour')
plt.colorbar(label='Loss')
plt.show()

print("Weights for univariate:", w)





# import numpy as np
# import pandas as pd
# import matplotlib.pyplot as plt
# # from mpl_toolkits.mplot3d import Axes3D

# def gen_equ_gd(X, y):
#     col = np.ones(X.shape[0])
#     data = np.insert(X, 0, col, axis=1)
#     w = np.random.randn(data.shape[1])
#     gradj = np.zeros(len(w))
#     loss_var = []
#     for i in range(100):
#         h = data @ w
#         loss = (np.sum((h - y) ** 2)) / (2 * data.shape[0])  # Update the denominator here
#         loss_var.append(loss)
#         for j in range(len(gradj)):
#             gradj[j] = np.dot((h - y), data[:, j]) / data.shape[0]
#         w -= (0.01 * gradj)
#     return loss_var, w

# # Load data from CSV file
# data = pd.read_csv(r"F:\IITM\Mtech 2_sem\data_science\lab_py_files\heart.data.csv")

# # Assuming the CSV has columns 'biking', 'smoking', and 'heart.disease'
# X = data[['biking', 'smoking']].values
# y = data['heart.disease'].values

# # Reshape y to match the number of samples in h
# y = y[:X.shape[0]]  # Assuming y has more samples than X, truncate y to match the length of X

# # Call the function with loaded data
# loss_var, w = gen_equ_gd(X, y)

# # Extracting coefficients
# b, m1, m2 = w

# # Create a meshgrid for the features
# biking_range = np.linspace(min(X[:, 0]), max(X[:, 0]), 10)
# smoking_range = np.linspace(min(X[:, 1]), max(X[:, 1]), 10)
# biking_mesh, smoking_mesh = np.meshgrid(biking_range, smoking_range)
# def heart_disease_predicted(b,m1,m2):
#     return (b + m1 * biking_mesh + m2 * smoking_mesh)

# # Plotting
# fig = plt.figure(figsize=(10, 8))
# ax = fig.add_subplot(111, projection='3d')

# # Data points
# ax.scatter(X[:, 0], X[:, 1], y, color='r', label='Data points')

# # Regression plane
# ax.plot_surface(biking_mesh, smoking_mesh, heart_disease_predicted, alpha=0.5,color='blue', label='Best Fit Plane')

# ax.set_xlabel('Biking')
# ax.set_ylabel('Smoking')
# ax.set_zlabel('Heart Disease')
# ax.set_title('Regression Plane for Heart Disease Prediction')
# ax.legend()
# plt.show()







import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Read the CSV file
data1 = pd.read_csv('heart.data.csv')
data = (data1 - data1.mean()) / data1.std()

# Extract independent variables (features) X1, X2, ... and the dependent variable (target) y
X = data[['biking', 'smoking']].values
y = data['heart.disease'].values

def multivariate_linear_regression(X, y):
    col = np.ones(X.shape[0])
    data = np.insert(X, 0, col, axis=1)
    w = np.random.randn(data.shape[1])
    gradj = np.zeros(len(w))
    loss_var = []
    for i in range(4000):
        h = data @ w
        loss = (np.sum((h - y) ** 2)) / (2 * data.shape[0])  # Update the denominator here
        loss_var.append(loss)
        for j in range(len(gradj)):
            gradj[j] = np.dot((h - y), data[:, j]) / data.shape[0]
        w -= (0.01 * gradj)
    return loss_var, w

# Compute weights for multivariate linear regression
loss_var, w = multivariate_linear_regression(X, y)

print("Weights for multivariate:", w)

# Generate grid points for X1 and X2 to create the mesh grid
biking_range = np.linspace(min(X[:, 0]), max(X[:, 0]), 10)
smoking_range = np.linspace(min(X[:, 1]), max(X[:, 1]), 10)
biking_mesh, smoking_mesh = np.meshgrid(biking_range, smoking_range)

# Define a function to compute z-values (predicted values) for the plane
def compute_z_values(biking_mesh, smoking_mesh, w):
    col = np.ones(biking_mesh.shape)
    data = np.stack((col, biking_mesh, smoking_mesh), axis=-1)
    z_values = np.sum(data * w, axis=-1)
    return z_values

# Compute z-values for the plane using the weights obtained from linear regression
z_values = compute_z_values(biking_mesh, smoking_mesh, w)

# Plot the data points and the best fit plane
fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111, projection='3d')

# Plot the data points
ax.scatter(X[:, 0], X[:, 1], y, color='blue', label='Data Points')

# Plot the best fit plane
ax.plot_surface(biking_mesh, smoking_mesh, z_values, alpha=0.5, cmap='viridis', label='Best Fit Plane')

# Set labels and title
ax.set_xlabel('Biking')
ax.set_ylabel('Smoking')
ax.set_zlabel('Heart Disease')
ax.set_title('Best Fit Plane for Multivariate Linear Regression')

# Add a legend
# ax.legend()

# Show plot
plt.show()


print("Weights for multivariate:", w)


# Compute correlation between features and target
correlation_smoking_heart_disease = np.corrcoef(X[:, 1], y)[0, 1]
correlation_biking_heart_disease = np.corrcoef(X[:, 0], y)[0, 1]

# Plot the scatter plots
plt.figure(figsize=(10, 6))

# Scatter plot for smoking vs heart disease
plt.subplot(1, 2, 1)
plt.scatter(X[:, 1], y, color='blue')
plt.xlabel('Smoking')
plt.ylabel('Heart Disease')
plt.title(f'Correlation: {correlation_smoking_heart_disease:.2f}')

# Scatter plot for biking vs heart disease
plt.subplot(1, 2, 2)
plt.scatter(X[:, 0], y, color='green')
plt.xlabel('Biking')
plt.ylabel('Heart Disease')
plt.title(f'Correlation: {correlation_biking_heart_disease:.2f}')

plt.tight_layout()
plt.show()

