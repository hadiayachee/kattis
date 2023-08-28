import math
#Write an rule of euclidean distance between 2 points with x and y
def distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)
#this is like the Closest pair without used D and C its need a big complexity O(n^2) that for each point calculate the distance between one point with all points and go to another point and make the same
def brute_force(points):
    n = len(points)
    if n < 2:
        return None, None, float('inf')

    min_dist = float('inf')
    pair = (points[0], points[1])

    for i in range(n):
        for j in range(i + 1, n):
            d = distance(points[i], points[j])
            if d < min_dist:
                min_dist = d
                pair = (points[i], points[j])

    return pair[0], pair[1], min_dist

def closest_pair(points):
    n = len(points)
#call the brute force
    if n <= 3:
        return brute_force(points)
#start divide and conquer that make half of every part and calculate the distance for each part that half it and then comparing
    mid = n // 2
    left_half = points[:mid]
    right_half = points[mid:]

    left_pair1, left_pair2, left_min_dist = closest_pair(left_half)
    right_pair1, right_pair2, right_min_dist = closest_pair(right_half)

    if left_min_dist < right_min_dist:
        min_pair1, min_pair2, min_dist = left_pair1, left_pair2, left_min_dist
    else:
        min_pair1, min_pair2, min_dist = right_pair1, right_pair2, right_min_dist

    strip = [point for point in points if abs(point[0] - points[mid][0]) < min_dist]
    strip.sort(key=lambda x: x[1])

    for i in range(len(strip)):
        for j in range(i + 1, len(strip)):
            if strip[j][1] - strip[i][1] >= min_dist:
                break
            d = distance(strip[i], strip[j])
            if d < min_dist:
                min_dist = d
                min_pair1, min_pair2 = strip[i], strip[j]

    return min_pair1, min_pair2, min_dist

def main():
    while True:
        n = int(input())
        if n == 0:
            break
        points = []
        for _ in range(n):
            x, y = map(float, input().split())
            points.append((x, y))

        points.sort()  # Sort the points by x-coordinate
        pair1, pair2, min_dist = closest_pair(points)

        print(f"{pair1[0]:.2f} {pair1[1]:.2f} {pair2[0]:.2f} {pair2[1]:.2f}")

