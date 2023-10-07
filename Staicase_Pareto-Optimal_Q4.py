# 4 Finally, suppose the points in P are already given in sorted order from
# left to right. Describe an algorithm to compute the staircase of P in O(n)time.
import random


def generate_random_points(n, xmin, xmax, ymin, ymax):
    points = []
    for _ in range(n):
        x = random.randint(xmin, xmax)
        y = random.randint(ymin, ymax)
        points.append((x, y))
    return points


def find_pareto_optimal(points):
    pareto_points = []
    max_y = float("-inf")

    for point in points:
        x, y = point
        if y >= max_y:
            pareto_points.append(point)
            max_y = y
    return pareto_points


# Example usage:
n = 50  # Adjust the value of n as needed
xmin = 0
xmax = 100
ymin = 0
ymax = 100

# Generate random points
points = generate_random_points(n, xmin, xmax, ymin, ymax)

# Sort points by x-coordinate (if not already sorted)
sorted_points = sorted(points, key=lambda point: -point[0])

# Find Pareto-optimal points
pareto_optimal_points = find_pareto_optimal(sorted_points)

pareto_optimal_points.reverse()
print(pareto_optimal_points)
