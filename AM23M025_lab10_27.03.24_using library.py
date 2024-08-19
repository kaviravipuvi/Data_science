# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 18:38:10 2024

@author: Kaviyarasan PR
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Read the CSV file
data = pd.read_csv('heart.data.csv')

# Normalize the dataframe using Z normalization (standardization)
normalized_data = (data - data.mean()) / data.std()

# Extract independent variables (features) X1, X2, ... and the dependent variable (target) y
X = normalized_data[['biking', 'smoking']].values
y = normalized_data['heart.disease'].values

# Fit a linear regression model
model = LinearRegression()
model.fit(X, y)

# Extract the coefficients (weights) and intercept
w1, w2 = model.coef_
b = model.intercept_

# Generate grid points for X1 and X2 to create the mesh grid
biking_range = np.linspace(min(X[:, 0]), max(X[:, 0]), 10)
smoking_range = np.linspace(min(X[:, 1]), max(X[:, 1]), 10)
biking_mesh, smoking_mesh = np.meshgrid(biking_range, smoking_range)

# Compute z-values for the plane using the fitted model
z_values = b + w1 * biking_mesh + w2 * smoking_mesh

# Plot the data points and the best fit plane
fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111, projection='3d')

# Plot the data points
ax.scatter(X[:, 0], X[:, 1], y, color='blue', label='Data Points')

# Plot the best fit plane
ax.plot_surface(biking_mesh, smoking_mesh, z_values, alpha=0.5, cmap='viridis', label='Best Fit Plane')

# Set labels and title
ax.set_xlabel('Biking (Normalized)')
ax.set_ylabel('Smoking (Normalized)')
ax.set_zlabel('Heart Disease (Normalized)')
ax.set_title('Best Fit Plane for Multivariate Linear Regression')

# Add a legend
ax.legend()

# Show plot
plt.show()

# Print the coefficients and intercept
print("Coefficients (Weights):", w1, w2)
print("Intercept (Bias):", b)
