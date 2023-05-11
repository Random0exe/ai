import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

# Generate some random data
X = np.random.rand(100, 2)

# Create a K-means instance with K=3 clusters
kmeans = KMeans(n_clusters=3)

# Fit the data to the K-means algorithm
kmeans.fit(X)

# Get the cluster labels for each data point
labels = kmeans.labels_

# Get the cluster centroids
centroids = kmeans.cluster_centers_

# Plot the data points and cluster centroids
plt.scatter(X[:, 0], X[:, 1], c=labels)
plt.scatter(centroids[:, 0], centroids[:, 1], marker='X', color='red', s=200)
plt.title('K-means Clustering')
plt.xlabel('X')
plt.ylabel('Y')
plt.show()
