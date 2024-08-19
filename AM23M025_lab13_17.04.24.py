# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 17:35:13 2024
c 
@author: Kaviyarasan PR

"""
"""
1) Create the following data and write to a csv file: Generate 10 random points in
 each of the the following circles (i) centre at (3,3) and radius 2, (ii) centre at (7,7) and radius 2 
 iii) centre at (11,11) and radius 2.  Plot the data as well.                 (2 marks)

2)  Implement K - means clustering algorithm (with out using sklearn library) and for the above data, 
show the change in the centroid as well as the class assignments. Also, plot the cost function for K 
varying from 1 to 5. Show that the value of K matches with the intuition from the data. 
Plot the K-classes for the final K-value.      (8 marks)
"""



import numpy as np
import matplotlib.pyplot as plt
import csv

# Define circle parameters
circles = [
    {"center": (3, 3), "radius": 2},
    {"center": (7, 7), "radius": 2},
    {"center": (11, 11), "radius": 2}
]

# Generate random points in each circle
num_points_per_circle = 10
random_points = []

# Generate random points in circles
for circle in circles:
    center = circle["center"]
    radius = circle["radius"]
    for _ in range(num_points_per_circle):
        angle = np.random.uniform(0, 2*np.pi)  # Generate random angle
        r = np.sqrt(np.random.uniform(0, radius**2))  # Generate random radius within circle
        x = center[0] + r * np.cos(angle)  # Calculate x-coordinate of point
        y = center[1] + r * np.sin(angle)  # Calculate y-coordinate of point
        random_points.append((x, y))

# Plot the initial random data
for circle in circles:
    center = circle["center"]
    plt.scatter(center[0], center[1], color='red', marker='o')  # Plot circle centers
plt.scatter(*zip(*random_points), color='blue', marker='o')  # Plot random points
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Random Points in Circles')
plt.axis('equal')
plt.grid(True)
plt.show()

# Write points to CSV file
with open('random_points.csv', 'w', newline='') as csvfile:
    csv_writer = csv.writer(csvfile)
    csv_writer.writerow(['X', 'Y'])
    csv_writer.writerows(random_points)

# Load the data from the CSV file
loaded_data = np.loadtxt('random_points.csv', delimiter=',', skiprows=1)

class KmeansClustering:
    def __init__(self, data, num_clusters):
        self.data = data
        self.num_clusters = num_clusters
    
    def fit(self, max_iterations):
        # Initialize centroids randomly
        self.centroids = self.data[np.random.choice(self.data.shape[0], self.num_clusters, replace=False)]
        self.labels = None
        
        # Lists to store centroid updates and costs
        self.centroid_updates = [self.centroids]
        self.costs = []
        
        # Loop until centroids no longer change or max_iterations reached
        for _ in range(max_iterations):
            # Assign each point to the nearest centroid
            distances = np.linalg.norm(self.data[:, np.newaxis] - self.centroids, axis=2)
            self.labels = np.argmin(distances, axis=1)
            
            # Update centroids
            new_centroids = np.array([self.data[self.labels == k].mean(axis=0) for k in range(self.num_clusters)])
            
            # Calculate total cost
            cost = np.sum(np.min(distances, axis=1))
            self.costs.append(cost)
            
            # Check if centroids have changed
            if np.allclose(new_centroids, self.centroids):
                break
            
            # Update centroids
            self.centroids = new_centroids
            
            # Store centroid updates
            self.centroid_updates.append(self.centroids)
    
    def predict(self):
        return self.labels, self.centroids

# Initialize an empty array to store costs for different number of clusters
costs_array = np.array([])

# Define range of number of clusters
num_clusters_range = range(1, 6)

# Iterate over different number of clusters
for num_clusters in num_clusters_range:
    # Perform KMeans clustering
    kmeans_model = KmeansClustering(loaded_data, num_clusters)
    kmeans_model.fit(100)  # Assuming max_iterations is 100
    
    # Calculate cost (within-cluster norm)
    distances = np.linalg.norm(loaded_data[:, np.newaxis] - kmeans_model.centroids, axis=2)
    cost = np.sum(np.min(distances, axis=1))
    
    # Append cost to the array
    costs_array = np.append(costs_array, cost)
    
    # Plot centroid updates for each iteration
    for i, centroid_update in enumerate(kmeans_model.centroid_updates):
        plt.figure(figsize=(8, 6))
        plt.scatter(loaded_data[:, 0], loaded_data[:, 1], c=kmeans_model.labels, cmap='viridis', marker='x', alpha=0.7)
        plt.scatter(centroid_update[:, 0], centroid_update[:, 1], marker='o', s=200, c='red', label=f'Centroids - Iteration {i+1}')
        plt.title(f'K-Means Clustering with {num_clusters} Clusters')
        plt.xlabel('X')
        plt.ylabel('Y')
        plt.legend()
        plt.grid(True)
        plt.show()

# Plot the costs against the number of clusters
plt.plot(num_clusters_range, costs_array)
plt.xlabel('Number of Clusters')
plt.ylabel('Cost')
plt.title('Cost Function for Different Number of Clusters')
plt.xticks(num_clusters_range)
plt.grid(True)
plt.show()

# import numpy as np
# import matplotlib.pyplot as plt
# import csv

# # Define circle parameters
# circles = [
#     {"center": (3, 3), "radius": 2},
#     {"center": (7, 7), "radius": 2},
#     {"center": (11, 11), "radius": 2}
# ]

# # Generate random points in each circle
# num_points_per_circle = 10
# random_points = []

# for circle in circles:
#     center = circle["center"]
#     radius = circle["radius"]
#     for _ in range(num_points_per_circle):
#         angle = np.random.uniform(0, 2*np.pi)
#         r = np.sqrt(np.random.uniform(0, radius**2))
#         x = center[0] + r * np.cos(angle)
#         y = center[1] + r * np.sin(angle)
#         random_points.append((x, y))

# # Plot the initial random data
# for circle in circles:
#     center = circle["center"]
#     radius = circle["radius"]
#     plt.scatter(center[0], center[1], color='red', marker='o')
#     # circle_plot = plt.Circle(center, radius, color='blue', fill=False)
#     # plt.gca().add_artist(circle_plot)

# x_values = [point[0] for point in random_points]
# y_values = [point[1] for point in random_points]
# plt.scatter(x_values, y_values, color='blue', marker='o')
# plt.xlabel('X')
# plt.ylabel('Y')
# plt.title('Random Points in Circles')
# plt.axis('equal')
# plt.grid(True)
# plt.show()

# # Write points to CSV file
# with open('random_points.csv', 'w', newline='') as csvfile:
#     csv_writer = csv.writer(csvfile)
#     csv_writer.writerow(['X', 'Y'])
#     csv_writer.writerows(random_points)

# # Load the data from the CSV file
# loaded_data = np.loadtxt('random_points.csv', delimiter=',', skiprows=1)

# class KmeansClustering:
#     def __init__(self, data, num_clusters):
#         self.data = data
#         self.num_clusters = num_clusters
    
#     def fit(self, max_iterations):
#         # Initialize centroids randomly
#         self.centroids = self.data[np.random.choice(self.data.shape[0], self.num_clusters, replace=False)]
#         self.labels = None
        
#         # Lists to store centroid updates and costs
#         self.centroid_updates = [self.centroids]
#         self.costs = []
        
#         # Loop until centroids no longer change or max_iterations reached
#         for _ in range(max_iterations):
#             # Assign each point to the nearest centroid
#             distances = np.linalg.norm(self.data[:, np.newaxis] - self.centroids, axis=2)
#             self.labels = np.argmin(distances, axis=1)
            
#             # Update centroids
#             new_centroids = np.array([self.data[self.labels == k].mean(axis=0) for k in range(self.num_clusters)])
            
#             # Calculate total cost
#             cost = np.sum(np.min(distances, axis=1))
#             self.costs.append(cost)
            
#             # Check if centroids have changed
#             if np.allclose(new_centroids, self.centroids):
#                 break
            
#             # Update centroids
#             self.centroids = new_centroids
            
#             # Store centroid updates
#             self.centroid_updates.append(self.centroids)
    
#     def predict(self):
#         return self.labels, self.centroids

# # Initialize an empty array to store costs for different number of clusters
# costs_array = np.array([])

# # Define range of number of clusters
# num_clusters_range = range(1, 6)

# # Iterate over different number of clusters
# for num_clusters in num_clusters_range:
#     # Perform KMeans clustering
#     kmeans_model = KmeansClustering(loaded_data, num_clusters)
#     kmeans_model.fit(100)  # Assuming max_iterations is 100
    
#     # Calculate cost (within-cluster norm)
#     distances = np.linalg.norm(loaded_data[:, np.newaxis] - kmeans_model.centroids, axis=2)
#     cost = np.sum(np.min(distances, axis=1))
    
#     # Append cost to the array
#     costs_array = np.append(costs_array, cost)
    
#     # Plot centroid updates for each iteration
#     for i, centroid_update in enumerate(kmeans_model.centroid_updates):
#         plt.figure(figsize=(8, 6))
#         plt.scatter(loaded_data[:, 0], loaded_data[:, 1], c=kmeans_model.labels, cmap='viridis', marker='x', alpha=0.7)
#         plt.scatter(centroid_update[:, 0], centroid_update[:, 1], marker='o', s=200, c='red', label='Centroids')
#         plt.title(f'K-Means Clustering with {num_clusters} Clusters - Iteration {i+1}')
#         plt.xlabel('X')
#         plt.ylabel('Y')
#         plt.legend()
#         plt.show()

# # Plot the costs against the number of clusters
# plt.plot(num_clusters_range, costs_array)
# plt.xlabel('Number of Clusters')
# plt.ylabel('Cost')
# plt.title('Cost Function for Different Number of Clusters')
# plt.xticks(num_clusters_range)
# plt.grid(True)
# plt.show()
