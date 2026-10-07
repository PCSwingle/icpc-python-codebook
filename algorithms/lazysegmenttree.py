arr = [0] * n

t = [0] * (4 * n)
lazy = [0] * (4 * n)

def _build(v, tl, tr):
    if tl == tr:
        t[v] = arr[tl]
    else:
        tm = (tl + tr) // 2
        _build(v*2, tl, tm)
        _build(v*2+1, tm+1, tr)
        t[v] = min(t[v*2], t[v*2 + 1]) # change op
_build(1, 0, n - 1)

def _push(v, tl, tr):
    tm = (tl + tr) // 2

    t[v*2] += lazy[v] # * (tm - tl + 1) # range sum
    lazy[v*2] += lazy[v]
    t[v*2+1] += lazy[v] # * (tr - tm) # range sum
    lazy[v*2+1] += lazy[v]
    lazy[v] = 0

def _update(v, tl, tr, l, r, add):
    if l > r:
        return
    if l == tl and tr == r:
        t[v] += add # * (tr - tl + 1) # range sum
        lazy[v] += add
    else:
        _push(v, tl, tr)
        tm = (tl + tr) // 2
        _update(v*2, tl, tm, l, min(r, tm), add)
        _update(v*2+1, tm+1, tr, max(l, tm+1), r, add)
        t[v] = min(t[v*2], t[v*2 + 1]) # change op

def _query(v, tl, tr, l, r):
    if l > r:
        return float('inf') # change with op
    if l == tl and tr == r:
        return t[v]
    _push(v, tl, tr)
    tm = (tl + tr) // 2
    return min(_query(v*2, tl, tm, l, min(r, tm)),
               _query(v*2+1, tm+1, tr, max(l, tm+1), r)) # change op

def query(l, r): # [l, r)
    return _query(1, 0, n - 1, l, r - 1)

def update(ix, value): # sets index
    _update(1, 0, n - 1, ix, ix, value - query(ix, ix + 1))

def update_range(l, r, add): # [l, r)
    _update(1, 0, n - 1, l, r - 1, add)