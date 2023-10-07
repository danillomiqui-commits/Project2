# 3 Describe an algorithm to compute the staircase of P in O(n log h) time,
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
    n = len(points)

    if n <= 1:
        return points

    # Sort points by x-coordinate in descending order
    sorted_points = sorted(points, key=lambda point: (-point[0], point[1]))

    max_y = float("-inf")
    pareto_points = []

    for point in sorted_points:
        if point[1] >= max_y:
            pareto_points.append(point)
            max_y = point[1]
    pareto_points.reverse()
    return pareto_points


# Example usage:
n = 50  # Adjust the value of n as needed
xmin = 0
xmax = 100
ymin = 0
ymax = 100

# Generate random points
points = generate_random_points(n, xmin, xmax, ymin, ymax)
print(find_pareto_optimal(points))
