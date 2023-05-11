import numpy as np

def tsp_2opt(cities):
    # Number of cities
    n = len(cities)

    # Create a distance matrix
    dist_matrix = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            dist_matrix[i, j] = np.linalg.norm(cities[i] - cities[j])

    # Initial tour - visiting cities in the order they appear
    tour = np.arange(n)

    # Track improvement
    improvement = True

    while improvement:
        improvement = False
        for i in range(1, n - 1):
            for j in range(i + 1, n):
                # Compute the current distance
                current_dist = dist_matrix[tour[i], tour[i-1]] + dist_matrix[tour[j], tour[(j+1)%n]]
                # Compute the new distance after swapping edges
                new_dist = dist_matrix[tour[i], tour[(j+1)%n]] + dist_matrix[tour[j], tour[i-1]]
                if new_dist < current_dist:
                    # Update the tour
                    tour[i:j+1] = np.flip(tour[i:j+1])
                    improvement = True

    return tour

# Generate random cities
np.random.seed(0)
num_cities = 20
cities = np.random.rand(num_cities, 2)  # 2D coordinates

# Run the 2-Opt algorithm
tour = tsp_2opt(cities)

# Print the optimal tour
print("Optimal Tour:", tour)
