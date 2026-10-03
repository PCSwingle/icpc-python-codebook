def cross(p1, p2):
    return p1[0]*p2[1] - p1[1]*p2[0]

def sub(p1, p2):
    return p1[0] - p2[0], p1[1] - p2[1]

def dist_sq(p1, p2):
    return (p1[0] - p2[0])**2 + (p1[1] - p2[1])**2

j = 1
res = (0, (0, 0))
i = 0
while i < j:
    while True:
        nd = dist_sq(points[i], points[j])
        if nd > res[0]:
            res = (nd, (i, j))
        if cross(sub(points[(j + 1) % n], points[j]), sub(points[i + 1], points[i])) >= 0:
            break
        j = (j + 1) % n
    i += 1
dist, (p1, p2) = res