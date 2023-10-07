# 2Describe a divide-and-conquer algorithm to compute the staircase of P
# in O(nlogn) time.
import random


def generate_random_points(n, xmin, xmax, ymin, ymax):
    points = []
    for _ in range(n):
        x = random.randint(xmin, xmax)
        y = random.randint(ymin, ymax)
        points.append((x, y))
    return points


def find_pareto_staircase(points):
    if len(points) <= 1:
        return points

    # Sort points based on x-coordinate in descending order
    sp = sorted(points, key=lambda point: point[0], reverse=True)

    # Divide points into left and right halves
    mid = len(sp) // 2
    left_half = sp[:mid]
    right_half = sp[mid:]

    # Recursively compute staircases for left and right halves
    ls = find_pareto_staircase(left_half)
    rs = find_pareto_staircase(right_half)

    # Merge and filter staircases based on y-coordinate
    return merge_and_filter_staircases(ls, rs)


def merge_and_filter_staircases(left_staircase, right_staircase):
    staircase = []
    i, j = 0, 0
    max_y = float("-inf")

    while i < len(left_staircase) and j < len(right_staircase):
        left_point = left_staircase[i]
        right_point = right_staircase[j]

        if left_point[1] >= max_y and right_point[1] >= max_y:
            # Both points are Pareto-optimal
            if left_point[0] >= right_point[0]:
                staircase.append(left_point)
                max_y = left_point[1]
                i += 1
            else:
                staircase.append(right_point)
                max_y = right_point[1]
                j += 1
        elif left_point[1] >= right_point[1]:
            # Left point is Pareto-optimal
            if left_point[0] >= right_point[0]:
                staircase.append(left_point)
                max_y = left_point[1]
                i += 1
            else:
                j += 1
        else:
            # Right point is Pareto-optimal
            if right_point[0] >= left_point[0]:
                staircase.append(right_point)
                max_y = right_point[1]
                j += 1
            else:
                i += 1

    # Append remaining points from left_staircase and right_staircase
    while i < len(left_staircase):
        left_point = left_staircase[i]
        if left_point[1] >= max_y:
            staircase.append(left_point)
            max_y = left_point[1]
        i += 1

    while j < len(right_staircase):
        right_point = right_staircase[j]
        if right_point[1] >= max_y:
            staircase.append(right_point)
            max_y = right_point[1]
        j += 1

    return staircase


# Example usage:
n = 50  # Adjust the value of n as needed
xmin = 0
xmax = 100
ymin = 0
ymax = 100

# Generate random points
points = generate_random_points(n, xmin, xmax, ymin, ymax)

# Find Pareto-optimal points using the code


print("Random Points:", points)
print("Pareto-optimal points:", find_pareto_staircase(points))
