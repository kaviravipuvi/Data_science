# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 14:54:48 2024

@author: Kaviyarasan PR
"""

# Importing necessary libraries
import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# Load Iris dataset
iris = datasets.load_iris()
X_iris = iris.data[:, :2]  # Using only first two features (sepal length and width)
y_iris = iris.target

# Load Digits dataset
digits = datasets.load_digits()
X_digits = digits.data
y_digits = digits.target

# Function to visualize the data
def visualize_data(X, y, dataset_name):
    plt.figure(figsize=(8, 6))
    plt.scatter(X[:, 0], X[:, 1], c=y, cmap=plt.cm.Set1, edgecolor='k')
    plt.xlabel('Sepal length')
    plt.ylabel('Sepal width')
    plt.title(f'{dataset_name} Dataset')
    plt.show()

# Visualize Iris dataset
visualize_data(X_iris, y_iris, 'Iris')

# Visualize Digits dataset
def visualize_digits(X, y, dataset_name):
    plt.figure(figsize=(12, 6))
    for i in range(10):
        plt.subplot(2, 5, i + 1)
        plt.imshow(X[y == i][0].reshape(8, 8), cmap='binary', interpolation='nearest')
        plt.title(f'Digit: {i}')
        plt.axis('off')
    plt.suptitle(f'Sample Digits from {dataset_name} Dataset', fontsize=16)
    plt.show()

visualize_digits(X_digits, y_digits, 'Digits')



# Splitting the data into training and testing sets
X_train_iris, X_test_iris, y_train_iris, y_test_iris = train_test_split(X_iris, y_iris, test_size=0.2, random_state=42)
X_train_digits, X_test_digits, y_train_digits, y_test_digits = train_test_split(X_digits, y_digits, test_size=0.2, random_state=42)

# Standardizing the features
scaler = StandardScaler()
X_train_iris = scaler.fit_transform(X_train_iris)
X_test_iris = scaler.transform(X_test_iris)
X_train_digits = scaler.fit_transform(X_train_digits)
X_test_digits = scaler.transform(X_test_digits)

# Initializing and training the SVM model for Iris dataset
svm_iris = SVC(kernel='linear', random_state=42)
svm_iris.fit(X_train_iris, y_train_iris)

# Initializing and training the SVM model for Digits dataset
svm_digits = SVC(kernel='rbf', random_state=42)
svm_digits.fit(X_train_digits, y_train_digits)

# Testing the model for Iris dataset
y_pred_iris = svm_iris.predict(X_test_iris)
accuracy_iris = accuracy_score(y_test_iris, y_pred_iris)
print("Accuracy for Iris dataset:", accuracy_iris)
print("Confusion Matrix for Iris dataset:")
print(confusion_matrix(y_test_iris, y_pred_iris))
print("Classification Report for Iris dataset:")
print(classification_report(y_test_iris, y_pred_iris))

# Testing the model for Digits dataset
y_pred_digits = svm_digits.predict(X_test_digits)
accuracy_digits = accuracy_score(y_test_digits, y_pred_digits)
print("\nAccuracy for Digits dataset:", accuracy_digits)
print("Confusion Matrix for Digits dataset:")
print(confusion_matrix(y_test_digits, y_pred_digits))
print("Classification Report for Digits dataset:")
print(classification_report(y_test_digits, y_pred_digits))


"""
Q. 2 Principal Component Analysis:

To do PCA, use the Eigen decomposition available in numpy. The dataset can be obtained from https://scikit-learn.org/stable/auto_examples/decomposition/plot_pca_3d.html#sphx-glr-auto-examples-decomposition-plot-pca-3d-py. 
DO NOT USE the code available for PCA in the same link (as mentioned above, use numpy's Eigen decomposition). 
Compare your results with the one available in the link (here, you are free to use the code available in the link to generate any numbers for comparison). 
Are you getting the same result?

"""




import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sklearn import datasets

# Load the dataset
iris = datasets.load_iris()
X = iris.data
y = iris.target

# Standardize the features
X_standardized = (X - np.mean(X, axis=0))

# Compute the covariance matrix
cov_matrix = (1 / len(X_standardized)) * np.cov(X_standardized, rowvar=False)

# Perform eigen decomposition
eigenvalues, eigenvectors = np.linalg.eig(cov_matrix)

# Sort eigenvalues and eigenvectors
idx = eigenvalues.argsort()[::-1]
eigenvalues = eigenvalues[idx]
eigenvectors = eigenvectors[:, idx]

# print(eigenvalues)

# Define the range of n_components
n_components_range = [1, 2, 3]

# Visualize the dataset for different n_components
fig, axes = plt.subplots(1, len(n_components_range), figsize=(15, 5), subplot_kw={'projection': '3d'})

for i, n_components in enumerate(n_components_range):
    # Select the top n_components principal components
    projection_matrix = eigenvectors[:, :n_components]
    X_pca = np.dot(X_standardized, projection_matrix)

    # Scatter plot for each class
    for j in np.unique(y):
        if n_components == 1:
            axes[i].scatter(X_pca[y == j, 0], np.zeros_like(X_pca[y == j, 0]), np.zeros_like(X_pca[y == j, 0]), label=f'Class {j}')
        elif n_components == 2:
            axes[i].scatter(X_pca[y == j, 0], X_pca[y == j, 1], np.zeros_like(X_pca[y == j, 1]), label=f'Class {j}')
        else:
            axes[i].scatter(X_pca[y == j, 0], X_pca[y == j, 1], X_pca[y == j, 2], label=f'Class {j}')

    axes[i].set_xlabel('Principal Component 1')
    if n_components > 1:
        axes[i].set_ylabel('Principal Component 2')
    if n_components == 3:
        axes[i].set_zlabel('Principal Component 3')
    axes[i].set_title(f'PCA with {n_components} components')
    axes[i].legend()

plt.show()




import matplotlib.pyplot as plt

from sklearn import datasets
from sklearn.decomposition import PCA


iris = datasets.load_iris()

X = iris.data
y = iris.target
target_names = iris.target_names

pca = PCA(n_components=4)
X_r = pca.fit(X).transform(X)


# Percentage of variance explained for each components
# print(
#     "explained variance ratio : %s"
#     % str(pca.explained_variance_ratio_)
# )

plt.figure()
colors = ["navy", "turquoise", "darkorange"]
lw = 2

for color, i, target_name in zip(colors, [0, 1, 2], target_names):
    plt.scatter(
        X_r[y == i, 0], X_r[y == i, 1], color=color, alpha=0.8, lw=lw, label=target_name
    )
plt.legend(loc="best", shadow=False, scatterpoints=1)
plt.title("PCA of IRIS dataset")






# COMPARISION

total_variance = np.sum(eigenvalues)

# Normalize eigenvalues to obtain explained variance ratios
normalized_eigenvalues = eigenvalues / total_variance

# Compare eigenvalues with explained variance ratios
print("Eigenvalues:", eigenvalues)
print("Explained Variance Ratios (from PCA):", pca.explained_variance_ratio_)
print("Normalized Eigenvalues:", normalized_eigenvalues)

# Compare the values or ratios visually or numerically to see if they are similar

