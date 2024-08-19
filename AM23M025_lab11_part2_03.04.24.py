import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def sigmoid(z):
    return 1 / (1 + np.exp(-z))

def cross_entropy_cost_fn(x, y, learning_rate=0.01, max_iter=4000, tol=1e-5):
    m, n = x.shape
    col = np.ones((m, 1))
    data = np.hstack((col, x))
    w = np.random.randn(n + 1)
    loss_var = []

    for i in range(max_iter):
        h = sigmoid(data @ w)
        loss = -np.mean(y * np.log(h) + (1 - y) * np.log(1 - h))
        loss_var.append(loss)

        gradient = np.dot(data.T, (h - y)) / m
        w_old = np.copy(w)
        w -= learning_rate * gradient

        # Stopping criterion: change in weights is very small
        if np.linalg.norm(w - w_old) < tol:
            break

    return loss_var, w

def plot_decision_boundary(x, y, w):
    plt.scatter(x[:, 0], x[:, 1], c=y, marker='o')

    # # Plot decision boundary
    # slope = -w[2] / w[1]
    # intercept = w[0]
    # xx = np.linspace(np.min(x[:, 0]), np.max(x[:, 0]), 100)
    # yy = slope * xx + intercept
    # plt.plot(xx, yy, 'g-', label='Decision Boundary')
    
    plt.plot([], [], 'g-', label='Decision Boundary')  
    x1_min, x1_max = x[:, 0].min() - 1, x[:, 0].max() + 1
    x2_min, x2_max = x[:, 1].min() - 1, x[:, 1].max() + 1
    xx1, xx2 = np.meshgrid(np.arange(x1_min, x1_max, 0.01), np.arange(x2_min, x2_max, 0.01))
    Z = sigmoid(np.c_[np.ones((xx1.ravel().shape[0], 1)), xx1.ravel(), xx2.ravel()] @ w)
    Z = Z.reshape(xx1.shape)
    plt.contour(xx1, xx2, Z, levels=[0.5], colors='g', linestyles='-', label='Decision Boundary')
 
    
    plt.title('Classfication by logistic regression')
    plt.xlabel('x1')
    plt.ylabel('x2')
    plt.legend()
    plt.show()
    

data = pd.read_csv(r"F:\IITM\Mtech 2_sem\data_science\lab_py_files\files_used_for_programming\Logistic_regression_ls.csv")

# Extracting features and labels
x = data[['x1', 'x2']].values
y = data['label'].values

# Call the logistic regression function
loss_var, w = cross_entropy_cost_fn(x, y)

# Plot the decision boundary
plot_decision_boundary(x, y, w)

print(w)
