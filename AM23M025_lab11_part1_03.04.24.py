# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 14:15:36 2024

@author: Kaviyarasan PR
"""

"""
1) (a ) Plot the sigmoid function. Print your interpretation on why this function is useful for a classification problem.

    (b) Plot the log functions in the cost function individually. Print your interpretation of the log functions

     c) Using your own data for a single feature problem, and assuming linear regression problem, 
        plot the cost function and the corresponding contours. Also, using cross entropy as the cost function, 
        plot it as well as its contours.
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# import random

def sigmoid(z):
    s= (1/(1+np.exp(-z)))
    return s
sig= np.linspace(-10,10,100)


fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(sig, sigmoid(sig))
ax.set_xlabel('X Label')
ax.set_ylabel('Sigmoid function')
ax.grid()
plt.show()


sig= np.linspace(-10,10,100)
log= -np.log(sigmoid(sig))
plt.figure()
plt.plot(sigmoid(sig), log)
plt.grid()
plt.show()




sig= np.linspace(-10,10,100)
alog= -np.log(1-sigmoid(sig))
plt.figure()
plt.plot(sigmoid(sig), alog)
plt.grid()
plt.show()


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




"""INTERPRETATIONS : """



'''1)sigmoid fn. is based on maximum likelihood and also it transforms the output of logistic regression into probability.
   2)Moreover classification is a binary problem where the output values could be either 0 or 1.
   3)So we could set a thershold value that would classify the outputs as either 0 or 1.
   4)Sigmoid fn. exhibits this behaviour for z=0 where sig(0)=0.5 can be used as thershold for classifying.
   5)It also shrinks our data set to have values between 0 and 1 which agrees with the fundamental idea of probability 
    (0<probability of ocuurance of an event<1) '''



'''1)By using the log function as cost functions we are able to allocate penalty to the predicted value.
   2)It helps in avoiding mis-classificationby allocatinf maximum penalties like infinty to misclassified values and 0 to proper classification.
    Classification is said to be proper when Predicted=Actual'''












def cross_entropy_cost_fn(x,y):
    col= np.ones(x.shape[0])
    data= np.insert(x,0,col, axis=1)
    w= np.random.randn(data.shape[1])
    gradj=np.zeros(len(w))
    loss_var=[]
    for i in range(1000):
        h= sigmoid(data@w)
        loss= np.sum(-y* np.log(h)-(1-y)*np.log(1-h))/data.shape[1]
        loss_var.append(loss)
        for j in range(len(gradj)):
            gradj[j]= np.dot((h-y),data[:,j])/data.shape[0]
        w-=(0.01*gradj)
    return loss_var, w


data = pd.read_csv(r"F:\IITM\Mtech 2_sem\data_science\lab_py_files\univariate_linear_regression.csv")

# Assuming the CSV has columns 'x' and 'y', and you want to use them for regression
x = data['x'].values.reshape(-1, 1)  # Reshape to make it a column vector
y = np.random.randint(0,2,len(x))

# Call the function with loaded data
# print(gen_equ_gd(x, y))
loss_var,w = cross_entropy_cost_fn(x, y)
plt.plot(range(1000), loss_var)
plt.title('Loss Function over Iterations')
plt.xlabel('Iteration')
plt.ylabel('Loss')
plt.show()

# # Plot the best fit line
# plt.scatter(x, y, label='Data')
# plt.plot(x, np.dot(np.insert(x, 0, np.ones(x.shape[0]), axis=1), w), color='red', label='Best Fit Line')
# plt.title('Best Fit Line')
# plt.xlabel('x')
# plt.ylabel('y')
# plt.legend()
# plt.show()

# Plot the loss function as a surface
fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111, projection='3d')
w0_vals = np.linspace(-0.02 ,0.02, 20)
w1_vals = np.linspace(-0.02 ,0.02, 20)
w0, w1 = np.meshgrid(w0_vals, w1_vals)


J_vals = np.zeros_like(w0)
for i in range(len(w0_vals)):
    for j in range(len(w1_vals)):
        h= sigmoid(data @np.array([w0[i,j],w1[i,j]]))
        J_vals[i, j] =  np.sum(-y* np.log(h)-(1-y)*np.log(1-h))/data.shape[1]
ax.plot_surface(w1, w0, J_vals, cmap='viridis')
ax.set_xlabel('w0')
ax.set_ylabel('w1')
ax.set_zlabel('Loss')
ax.set_title('Loss Function Surface')
plt.show()

# Plot the loss function as a contour
plt.figure(figsize=(10, 6))
plt.contour(w0, w1, J_vals, levels= 150)
plt.xlabel('w0')
plt.ylabel('w1')
plt.title('Loss Function Contour')
plt.colorbar(label='Loss')
plt.show()

print("Weights for cross entropy:", w)

