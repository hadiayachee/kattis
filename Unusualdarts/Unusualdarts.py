def intersect(p1, p2, p3, p4):
#extrect coordinates from input tuples.
    (x1, y1), (x2, y2), (x3, y3), (x4, y4) = p1, p2, p3, p4
#calculate coefficients of the line equations for the two line segmentss.
    a, b, c = y2 - y1, x1 - x2, (y2 - y1) * x1 - (x2 - x1) * y1
    d, e, f = y4 - y3, x3 - x4, (y4 - y3) * x3 - (x4 - x3) * y3
#check if the first line segment is a single point.
    if a == b == 0:
#if the second line segment is also a single point, check if they are the same point.
        return ((x1, y1) if (x1, y1) == (x3, y3) else None) if d == e == 0 else (
#if the second line segment is not a single point, check if the point lies on it.
            (x1, y1) if d * x1 + e * y1 == f and min(x3, x4) <= x1 <= max(x3, x4) and min(y3, y4) <= y1 <= max(y3, y4) else None)
#check if the second line segment is a single point.
    elif d == e == 0:
#check if the point lies on the first line segment.
        return (x3, y3) if a * x3 + b * y3 == c and min(x1, x2) <= x3 <= max(x1, x2) and min(y1, y2) <= y3 <= max(y1, y2) else None
    else:
#calculate the determinant to check if the lines are not parallel.
        det = b * d - a * e
        if det:
#calculate the intersection point (x, y).
            x, y = (b * f - c * e) / det, (c * d - a * f) / det
#check if the intersection point lies within the bounds of both line segments.
            return (x, y) if min(x1, x2) <= x <= max(x1, x2) and min(y1, y2) <= y <= max(y1, y2) and min(x3, x4) <= x <= max(x3, x4) and min(y3, y4) <= y <= max(y3, y4) else None
        else:
            if a * f != c * d or b * f != c * e:
                return None
            else:
#calculate the intersection points (i1, i2) of the line segments.
                p, q = min((x1, y1), (x2, y2)), max((x1, y1), (x2, y2))
                r, s = min((x3, y3), (x4, y4)), max((x3, y3), (x4, y4))
                if (p, q) == (r, s):
                    i1, i2 = p, q
                elif p <= r <= q:
                    i1, i2 = r, min(q, s)
                elif r <= p <= s:
                    i1, i2 = p, min(s, q)
                else:
                    i1 = i2 = None
                if i1 == i2 and i1 is not None:
                    return i1
                elif i1:
                    return (i1, i2)
                else:
                    return None
#define a function to calculate the area of a polygon defined by a list of vertices 'poly'.
def area(poly):
    a, n = 0, len(poly)
    for i in range(n):
        a += poly[i][0] * poly[(i + 1) % n][1] - poly[i][1] * poly[(i + 1) % n][0]
    return abs(a) / 2
#define a set of line segment pairs to check for intersections.
check = ((0, 2), (0, 3), (0, 4), (0, 5),
         (1, 3), (1, 4), (1, 5), (1, 6),
         (2, 4), (2, 5), (2, 6),
         (3, 5), (3, 6),
         (4, 6))
from itertools import permutations
#loop for the number of test cases.
for _ in range(int(input())):
    P = [[*map(float, input().split())] for _ in range(7)]
    c = float(input())
#iterate through all permutations of the 7 points.
    for r in permutations(range(7)):
#rearrange the points based on the current permutation 'r'.
        p = [P[i] for i in r]
        p.append(P[0])
        ok = True
#check for intersections between line segments defined in 'check'.
        for i, j in check:
            if intersect(p[i], p[i + 1], p[j], p[j + 1]):
                ok = False
                break
#if the polygon is valid (no intersections), calculate its area, cube it, and compare to 'c'.
        if ok:
            a = area(p) / 4
            a **= 3
            o = r.index(0)  
            if abs(a - c) < 1e-5:
#print the indices of the rearranged points.
                print(*[i + 1 for i in r])
                break 
