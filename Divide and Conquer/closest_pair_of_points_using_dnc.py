import math
import copy

class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

# A utility function to find the
# distance between two points
def dist(p1, p2):
    return math.sqrt((p1.x - p2.x) *
                     (p1.x - p2.x) +
                     (p1.y - p2.y) *
                     (p1.y - p2.y))

def stripClosest(strip,size,d):
    min_val = d
 
    
    # Pick all points one by one and
    # try the next points till the difference
    # between y coordinates is smaller than d.
    # This is a proven fact that this loop
    # runs at most 6 times
    for i in range(size):
        j = i + 1
        while j < size and (strip[j].y -
                            strip[i].y) < min_val:
            min_val = dist(strip[i], strip[j])
            j += 1
 
    return min_val

# A Brute Force method to return the
# smallest distance between two points
# in P[] of size n
def bruteForce(P, n):
    min_val = float('inf')
    for i in range(n):
        for j in range(i + 1, n):
            if dist(P[i], P[j]) < min_val:
                min_val = dist(P[i], P[j])
 
    return min_val

def closestUtil(P,Q,n):
    if n <= 3:
        return bruteForce(P, n)
    
    mid = n//2
    midPoint = P[mid]

    #copy of left n right
    cleft = P[:mid]
    cright = P[mid:]

    left = closestUtil(cleft,Q,mid)
    right = closestUtil(cright,Q,n-mid)

    d = min(left,right)

    # Build an array strip[] that contains
    # points close (closer than d)
    # to the line passing through the middle point
    stripP = []
    stripQ = []
    lr = cleft+cright
    for i in range(n):
        if abs(lr[i].x - midPoint.x)<d:
            stripP.append(lr[i])
        if abs(Q[i].x - midPoint.x) <d:
            stripQ.append(Q[i])
    
    stripP.sort(key = lambda point:point.y)
    min_a = min(d,stripClosest(stripP,len(stripP),d))
    min_b = min(d,stripClosest(stripQ,len(stripQ),d))

    return min(min_a,min_b)

def closest(P,n):
    P.sort(key = lambda p:p.x)
    Q = copy.deepcopy(P)
    Q.sort(key = lambda q:q.y)

    #Using recursive function closestUtil() to find the smallest distance
    return closestUtil(P,Q,n)

#main driver code
P = [Point(2, 3), Point(12, 30),
     Point(40, 50), Point(5, 1),
     Point(12, 10), Point(3, 4)]

n=len(P)
print("The Smallest distance is:",closest(P,n))

# Output
# The Smallest distance is: 1.4142135623730951
