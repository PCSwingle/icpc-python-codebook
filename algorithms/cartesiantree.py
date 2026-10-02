# max tree (change ops for min)
l_children = [None] * n
r_children = [None] * n
parents = [None] * n

s = []
for i in range(n):
    last = None
    while s and arr[i] > arr[s[-1]]: # change op, duplicate parent is on left
        last = s.pop()
    if last is not None:
        l_children[i] = last
        parents[last] = i
    if s:
        r_children[s[-1]] = i
        parents[i] = s[-1]
    s.append(i)
root = s[0]