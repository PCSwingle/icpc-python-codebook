tree = [0] * (2 * n)
for i in range(n):
    tree[n + i] = arr[i]
for i in range(n - 1, 0, -1):
    tree[i] = tree[i << 1] + tree[i << 1 | 1] # change op

def update(p, value): 
    p = p + n
    tree[p] = value
    while p > 1:
        tree[p >> 1] = tree[p] + tree[p ^ 1] # change op
        p >>= 1

def query(l, r): # [l, r)
    res = 0
    l += n
    r += n
    while l < r:
        if l & 1:
            res += tree[l] # change op
            l += 1
        if r & 1:
            r -= 1
            res += tree[r] # change op
        l >>= 1
        r >>= 1
    return res
