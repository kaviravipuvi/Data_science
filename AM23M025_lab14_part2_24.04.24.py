# -*- coding: utf-8 -*-
"""
Created on Mon Apr 29 23:08:43 2024

@author: Kaviyarasan PR
"""

import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

# Sigmoid is used as the activation function
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

# Derivative of the sigmoid function
def sigmoid_prime(x):
    return sigmoid(x) * (1.0 - sigmoid(x))

class NeuralNetwork(object):
    
    def __init__(self, architecture):
        # Architecture - numpy array with ith element representing the number of neurons in the ith layer.
        
        # Initialize the network architecture
        self.L = architecture.size - 1  # L corresponds to the last layer of the network.
        self.n = architecture  # n stores the number of neurons in each layer
        # input_size is the number of neurons in the first layer i.e. n[0]
        # output_size is the number of neurons in the last layer i.e. n[L]
        
        # Parameters will store the network parameters, i.e. the weights and biases
        self.parameters = {}
        
        # Initialize the network weights and biases:
        for i in range(1, self.L + 1): 
            # Initialize weights to small random values
            self.parameters['W' + str(i)] = np.random.randn(self.n[i], self.n[i - 1]) * 0.01
            
            # Initialize rest of the parameters to 1
            self.parameters['b' + str(i)] = np.ones((self.n[i], 1))
            self.parameters['z' + str(i)] = np.ones((self.n[i], 1))
            self.parameters['a' + str(i)] = np.ones((self.n[i], 1))
        
        # As we started the loop from 1, we haven't initialized a[0]:
        self.parameters['a0'] = np.ones((self.n[i], 1))
        
        # Initialize the cost:
        self.parameters['C'] = 1
        
        # Create a dictionary for storing the derivatives:
        self.derivatives = {}
                    
    def forward_propagate(self, X):
        # Note that X here, is just one training example
        self.parameters['a0'] = X
        
        # Calculate the activations for every layer l
        for l in range(1, self.L + 1):
            self.parameters['z' + str(l)] = np.add(np.dot(self.parameters['W' + str(l)], self.parameters['a' + str(l - 1)]), self.parameters['b' + str(l)])
            self.parameters['a' + str(l)] = sigmoid(self.parameters['z' + str(l)])
        
    def compute_cost(self, y):
        self.parameters['C'] = -(y * np.log(self.parameters['a' + str(self.L)]) + (1 - y) * np.log(1 - self.parameters['a' + str(self.L)]))
    
    def compute_derivatives(self, y):
        # Partial derivatives of the cost function with respect to z[L], W[L] and b[L]:        
        # dzL
        self.derivatives['dz' + str(self.L)] = self.parameters['a' + str(self.L)] - y
        # dWL
        self.derivatives['dW' + str(self.L)] = np.dot(self.derivatives['dz' + str(self.L)], np.transpose(self.parameters['a' + str(self.L - 1)]))
        # dbL
        self.derivatives['db' + str(self.L)] = self.derivatives['dz' + str(self.L)]

        # Partial derivatives of the cost function with respect to z[l], W[l] and b[l]
        for l in range(self.L-1, 0, -1):
            self.derivatives['dz' + str(l)] = np.dot(np.transpose(self.parameters['W' + str(l + 1)]), self.derivatives['dz' + str(l + 1)]) * sigmoid_prime(self.parameters['z' + str(l)])
            self.derivatives['dW' + str(l)] = np.dot(self.derivatives['dz' + str(l)], np.transpose(self.parameters['a' + str(l - 1)]))
            self.derivatives['db' + str(l)] = self.derivatives['dz' + str(l)]
            
    def update_parameters(self, alpha):
        for l in range(1, self.L + 1):
            self.parameters['W' + str(l)] -= alpha * self.derivatives['dW' + str(l)]
            self.parameters['b' + str(l)] -= alpha * self.derivatives['db' + str(l)]
        
    def predict(self, x):
        self.forward_propagate(x)
        return self.parameters['a' + str(self.L)]
        
    def fit(self, X_train, y_train, X_val, y_val, num_iter, alpha=0.01):
        train_losses = []  # Store train losses over iterations
        val_losses = []  # Store validation losses over iterations

        for iter in range(num_iter):
            train_loss = 0  # Stores the average training loss for this iteration
            val_loss = 0  # Stores the average validation loss for this iteration
            n_c_train = 0  # Stores the number of correct predictions on training set
            n_c_val = 0  # Stores the number of correct predictions on validation set
    
            # Training loop
            for i in range(X_train.shape[0]):
                x_train = X_train[i].reshape((X_train[i].size, 1))
                y_train_single = y_train[i]
    
                self.forward_propagate(x_train)
                self.compute_cost(y_train_single)
                self.compute_derivatives(y_train_single)
                self.update_parameters(alpha)
    
                train_loss += self.parameters['C']
    
                y_pred_train = self.predict(x_train)
                y_pred_train = (y_pred_train > 0.5)
    
                if y_pred_train == y_train_single:
                    n_c_train += 1
    
            train_loss /= X_train.shape[0]
            train_losses.append(train_loss)
            training_loss=np.array([item for sublist1 in val_losses for sublist2 in sublist1 for item in sublist2])

    
            # Validation loop
            for i in range(X_val.shape[0]):
                x_val = X_val[i].reshape((X_val[i].size, 1))
                y_val_single = y_val[i]
    
                self.forward_propagate(x_val)
                self.compute_cost(y_val_single)
    
                val_loss += self.parameters['C']
    
                y_pred_val = self.predict(x_val)
                y_pred_val = (y_pred_val > 0.5)
    
                if y_pred_val == y_val_single:
                    n_c_val += 1

            val_loss /= X_val.shape[0]
            val_losses.append(val_loss)
            validation_loss= np.array([item for sublist1 in val_losses for sublist2 in sublist1 for item in sublist2])

            print(np.array([val_losses]).shape)

            # Print or store training and validation losses
            print(f"Iteration: {iter}, Train Loss: {train_loss}, Validation Loss: {val_loss}")

        # Check for early stopping based on validation loss
            # if iter > 0 and val_losses[-1] > val_losses[-2]:
            #     print("Validation loss increased. Stopping training.")
            #     break

        # Plotting the losses over iterations
        plt.figure()
        plt.plot(range(len(training_loss)), training_loss, label='Train Loss')
        plt.plot(range(len(validation_loss)), validation_loss, label='Validation Loss')
        plt.xlabel('Iterations')
        plt.ylabel('Loss') 
        plt.title('Loss over Iterations')                                                       
        plt.legend()
        plt.show()
        
        # plt.xlabel('Iterations')
        # plt.ylabel('Loss') 
        # plt.title('Loss over Iterations')
        # plt.legend()
        # plt.show()



# Importing the dataset        
dataset = pd.read_csv(r"F:\IITM\Mtech 2_sem\data_science\lab_py_files\files_used_for_programming\Logistic_regression_ls.csv")

X = dataset.iloc[:, 0:-1].values
y = dataset.iloc[:, -1].values

# Feature Scaling
sc_X = StandardScaler()
X = sc_X.fit_transform(X)

# Manually splitting the data into train, validation, and test sets
split_ratio = 0.7  # 70% train, 15% validation, 15% test
split_train = int(len(X) * split_ratio)
split_val = int(len(X) * (split_ratio + 0.15))

X_train, X_val, X_test = X[:split_train], X[split_train:split_val], X[split_val:]
y_train, y_val, y_test = y[:split_train], y[split_train:split_val], y[split_val:]

# Defining the model architecture
architecture = np.array([2, 2, 2, 1])

# Creating the classifier
classifier = NeuralNetwork(architecture)

# Training the classifier
classifier.fit(X_train, y_train, X_val, y_val, 1000)

# Predicting the test set results:
n_c = 0
for i in range(X_test.shape[0]):
    x = X_test[i].reshape((X_test[i].size, 1))
    y = y_test[i]
    y_pred = classifier.predict(x)
    y_pred = (y_pred > 0.5)
    if y_pred == y:
        n_c += 1

print("Test Accuracy:", (n_c / X_test.shape[0]) * 100)

# Initializing variables to store true positives, false positives, false negatives, and true negatives
tp = 0
fp = 0
fn = 0
tn = 0

# Iterating through the test set and making predictions
for i in range(X_test.shape[0]):
    x = X_test[i].reshape((X_test[i].size, 1))
    y = y_test[i]
    y_pred = classifier.predict(x)
    y_pred = (y_pred > 0.5)

    # Updating counts for evaluation metrics
    if y_pred == 1 and y == 1:
        tp += 1
    elif y_pred == 1 and y == 0:
        fp += 1
    elif y_pred == 0 and y == 1:
        fn += 1
    else:
        tn += 1

# Calculate evaluation metrics
precision = tp / (tp + fp) if (tp + fp) > 0 else 0
recall = tp / (tp + fn) if (tp + fn) > 0 else 0
f1_score = 2 * precision * recall / (precision + recall) if (precision + recall) > 0 else 0
accuracy = (tp + tn) / (tp + fp + fn + tn)

# Print evaluation metrics
print("Precision:", precision)
print("Recall:", recall)
print("F1-Score:", f1_score)
print("Accuracy:", accuracy)


