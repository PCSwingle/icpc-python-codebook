def exp(b, e, m):
    a = 1
    while e > 0:
        if e & 1: a = (a*b)%m
        b = (b*b)%m
        e >>= 1
    return a
