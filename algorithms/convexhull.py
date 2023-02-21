from functools import cmp_to_key
import sys, math

def cross(p1, p2, p3): return (p2[0]-p1[0])*(p3[1]-p1[1])-(p2[1]-p1[1])*(p3[0]-p1[0])

def orien(p1, p2, p3):
    c = cross(p1, p2, p3)
    if c == 0:
        if math.dist(p1, p2) > math.dist(p1, p3): return 1
        else: return -1
    elif c < 0: return 1
    else: return -1

def convex_hull(points): # returns hull in CCW order with no colinear edges
    points = list(set(points))
    root = min(points)
    points.remove(root)
    points.sort(key=cmp_to_key(lambda x, y: orien(root, x, y)))
    stack = [root]
    for point in points:
        while len(stack) > 1 and cross(stack[-2], stack[-1], point) <= 0: stack.pop() # remove equals sign to keep colinear edges
        stack.append(point)
    return stack
