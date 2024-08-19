# -*- coding: utf-8 -*-
"""
Created on Thu Apr 18 18:22:20 2024

@author: Kaviyarasan PR
"""
"""
3) Taking any two classes from the above data, add labels to them (0 or 1) and create a new csv file. 
Split the data into Train / Test set as 70/30. 
(a) Plot the decision boundary using the developed logistic regression code 
(either with or without regularization) from one of your previous labs. 
(b) Evaluate the metrics such as Precision, Recall, F1-Score and Accuracy on the test data without 
using any library.  (10 marks)

"""


import numpy as np
import matplotlib.pyplot as plt
import csv

# Define circle parameters
circles = [
    {"center": (3, 3), "radius": 2},
    {"center": (7, 7), "radius": 2},
    
]

# Generate random points in each circle
num_points_per_circle = 10
random_points = []

# Generate random points in circles and assign labels
labels = []
for i, circle in enumerate(circles):
    center = circle["center"]
    radius = circle["radius"]
    for _ in range(num_points_per_circle):
        angle = np.random.uniform(0, 2*np.pi)  # Generate random angle
        r = np.sqrt(np.random.uniform(0, radius**2))  # Generate random radius within circle
        x = center[0] + r * np.cos(angle)  # Calculate x-coordinate of point
        y = center[1] + r * np.sin(angle)  # Calculate y-coordinate of point
        random_points.append((x, y))
        labels.append(i)

# Combine points and labels
data = np.column_stack((random_points, labels))

# Write data to CSV file
with open('random_points.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['x', 'y', 'label'])
    writer.writerows(data)

# Split data into features (X) and labels (y)
X = data[:, :2]
y = data[:, 2]

# Split data into Train / Test set as 70/30
def train_test_split(X, y, test_size=0.3, random_state=None):
    if random_state:
        np.random.seed(random_state)
    indices = np.random.permutation(X.shape[0])
    test_size = int(X.shape[0] * test_size)
    test_indices = indices[:test_size]
    train_indices = indices[test_size:]
    return X[train_indices], X[test_indices], y[train_indices], y[test_indices]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Plot the initial random data
for circle in circles:
    center = circle["center"]
    plt.scatter(center[0], center[1], color='red', marker='o')  # Plot circle centers
plt.scatter(X_train[:, 0], X_train[:, 1], color='blue', marker='o', label='Train')  # Plot train points
plt.scatter(X_test[:, 0], X_test[:, 1], color='green', marker='o', label='Test')  # Plot test points
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Random Points in Circles')
plt.axis('equal')
plt.grid(True)
plt.legend()
plt.show()






def sigmoid(z):
    return 1 / (1 + np.exp(-z))

def predict(X, w):
    col = np.ones((X.shape[0], 1))
    data = np.hstack((col, X))
    return sigmoid(np.dot(data, w))

def cross_entropy_cost_fn(X, y, num_iters=1000, learning_rate=0.3):
    # Add a column of ones to the feature matrix to account for bias
    X_bias = np.column_stack((np.ones((X.shape[0], 1)), X))
    
    # Initialize weights with the appropriate size (including the bias term)
    w = np.random.randn(X_bias.shape[1])
    
    # Initialize a list to store the loss values for each iteration
    losses = []

    # Gradient descent
    for i in range(num_iters):
        # Calculate the predicted probabilities using the sigmoid function
        h = sigmoid(np.dot(X_bias, w))
        
        # Calculate the cross-entropy loss
        loss = -np.mean(y * np.log(h) + (1 - y) * np.log(1 - h))
        losses.append(loss)
        
        # Calculate the gradient
        gradient = np.dot(X_bias.T, (h - y)) / y.size
        
        # Update the weights by subtracting the learning rate times the gradient
        w -= learning_rate * gradient

    return losses, w


# Train logistic regression model
losses, weights = cross_entropy_cost_fn(X_train, y_train)



def plot_decision_boundary(X, y, w):
    # Plot the data points with different colors for each class
    plt.scatter(X[:, 0], X[:, 1], c=y, cmap=plt.cm.Accent, marker='o', alpha=0.7, label='Data')
    
    # Define the range of the feature space for the plot
    x1_min, x1_max = X[:, 0].min() - 1, X[:, 0].max() + 1
    x2_min, x2_max = X[:, 1].min() - 1, X[:, 1].max() + 1
    
    # Create a meshgrid of points covering the feature space
    xx1, xx2 = np.meshgrid(np.arange(x1_min, x1_max, 0.01), np.arange(x2_min, x2_max, 0.01))
    
    # Flatten the meshgrid and predict probabilities for each point
    grid_points = np.c_[xx1.ravel(), xx2.ravel()]
    probabilities = predict(grid_points, w)
    
    # Reshape the probabilities to match the shape of the meshgrid
    probabilities = probabilities.reshape(xx1.shape)
    
    # Plot the decision boundary at the threshold of 0.5
    plt.contour(xx1, xx2, probabilities, levels=[0.5], colors='k', linestyles='--', label='Decision Boundary')
    
    # Add labels and title to the plot
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Decision Boundary')
    
    # Show the legend and plot
    plt.legend()
    plt.show()

# Plot the decision boundary using the trained weights
plot_decision_boundary(X_train, y_train, weights)



# Plot the loss curve
plt.plot(losses)
plt.xlabel('Iterations')
plt.ylabel('Loss')
plt.title('Loss Curve')
plt.show()

# Predict on test data
test_predictions = predict(X_test, weights)

# Convert probabilities to class labels
test_predictions = np.round(test_predictions)

# Evaluation metrics
tp = np.sum((test_predictions == 1) &  (y_test == 1))
fp = np.sum((test_predictions == 1) & (y_test == 0))
fn = np.sum((test_predictions == 0) & (y_test == 1))
tn = np.sum((test_predictions == 0) & (y_test == 0))

precision = tp / (tp + fp)
recall = tp / (tp + fn)
f1_score = 2 * (precision * recall) / (precision + recall)
accuracy = (tp + tn) / (tp + fp + fn + tn)

print("Precision:", precision)
print("Recall:", recall)
print("F1-Score:", f1_score)
print("Accuracy:", accuracy)
