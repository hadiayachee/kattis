import math
#define a function to calculate the Euclidean distance.
def euclidean_distance(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)
#empty list to store pairs of points with the minimum distance.
closest_pairs = []
#infinite loop that will continue until the user enters 0.
while True:
#read an integer 'n' from the user.
    n = int(input())
#if 'n' is 0, exit the loop.
    if n == 0:
        break
#create a list to store the (x, y) coordinates of points.
    Coordinates = []
#read 'n' lines, each containing two floating-point numbers separated by a space, and store them as (x, y) tuples.
    for _ in range(n):
        x, y = map(float, input().split())
        Coordinates.append((x, y))
#initialize a variable 'min' to represent the minimum distance as infinity.
    min_distance = float('inf')
#initialize 'closest_pair' as None to represent the closest pair of points.
    closest_pair = None
#loop through all possible pairs of points to calculate their distances and find the closest pair.
    for i in range(n):
        for j in range(i + 1, n):
            distance = euclidean_distance(Coordinates[i], Coordinates[j])         
#if the calculated distance is less than the current minimum distance, update 'min_distance' and 'closest_pair'.
            if distance < min_distance:
                min_distance = distance
                closest_pair = (Coordinates[i], Coordinates[j])
#add the closest pair of points to the 'closest_pairs' list.
    closest_pairs.append(closest_pair)
#print the results by iterating through the 'closest_pairs' list.
for closest_pair in closest_pairs:
    x1, y1 = closest_pair[0]
    x2, y2 = closest_pair[1]
    print(f'{x1:.2f} {y1:.2f} {x2:.2f} {y2:.2f}')
