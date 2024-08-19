# -*- coding: utf-8 -*-
"""
Created on Wed Apr 24 16:33:12 2024

@author: Kaviyarasan PR
"""
import numpy as np
import pandas as pd

data = pd.read_csv(r"F:\IITM\Mtech 2_sem\data_science\lab_py_files\random_points.csv")


X = data.iloc[:, :2].values
y = data.iloc[:, 2].values

def activation_function(s, activation):
   
    if activation == 'sigmoid':
        return 1 / (1 + np.exp(-s))
    elif activation == 'tanh':
        return np.tanh(s)
    elif activation == 'relu':
        return np.maximum(0, s)

class NeuralNetwork:
    def __init__(self, hidden_activation='sigmoid'):

        self.weights1 = np.random.random((2, 4))  
        self.biases1 = np.random.random(4)  
        self.weights2 = np.random.random((4, 1))  
        self.biases2 = np.random.random(1)  
        
        
        self.hidden_activation = hidden_activation
    def forward(self, X):
        # Forward pass through layer 1
        z1 = np.dot(X, self.weights1) + self.biases1
        a1 = activation_function(z1, self.hidden_activation)
        
        # Forward pass through layer 2
        z2 = np.dot(a1, self.weights2) + self.biases2
        a2 = activation_function(z2, 'sigmoid')
        
        return a2
    
    def predict(self, X):
        return np.round(self.forward(X))


hidden_activation = 'relu' 
nn = NeuralNetwork(hidden_activation=hidden_activation)

# Define the train_test_split function
def train_test_split(X, y, test_size=0.3, random_state=None):
    if random_state:
        np.random.seed(random_state)
    indices = np.random.permutation(X.shape[0])
    test_size = int(X.shape[0] * test_size)
    test_indices = indices[:test_size]
    train_indices = indices[test_size:]
    return X[train_indices], X[test_indices], y[train_indices], y[test_indices]

# Split the data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Predict the test set labels
test_predictions = nn.predict(X_test)

# Calculate evaluation metrics
tp = np.sum((test_predictions == 1) & (y_test == 1))
fp = np.sum((test_predictions == 1) & (y_test == 0))
fn = np.sum((test_predictions == 0) & (y_test == 1))
tn = np.sum((test_predictions == 0) & (y_test == 0))

precision = tp / (tp + fp) if (tp + fp) > 0 else 0
recall = tp / (tp + fn) if (tp + fn) > 0 else 0
f1_score = 2 * precision * recall / (precision + recall) if (precision + recall) > 0 else 0
accuracy = (tp + tn) / (tp + fp + fn + tn)

print("Precision:", precision)
print("Recall:", recall)
print("F1-Score:", f1_score)
print("Accuracy:", accuracy)

# Calculate loss
mse = np.mean((test_predictions - y_test)**2)
print(f"MSE: {mse}")

log_loss = np.mean(-y_test * np.log(nn.forward(X_test)) - (1 - y_test) * np.log(1 - nn.forward(X_test)))
print(f"log_loss: {log_loss}")
