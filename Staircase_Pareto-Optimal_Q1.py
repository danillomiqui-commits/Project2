# 1 Describe an algorithm to compute the staircase of P in O(nh) time,
# where h is the number of Pareto-optimal points
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
# Adjust the value of n as needed
n = 50
xmin = 0
xmax = 100
ymin = 0
ymax = 100

# Generate random points

points = generate_random_points(n, xmin, xmax, ymin, ymax)
pareto_optimal_points = find_pareto_optimal(points)
sorted_pareto_optimal = sorted(pareto_optimal_points, key=lambda point: point[0])

print("Random Points:", points)
print("Pareto-optimal points:", sorted_pareto_optimal)
