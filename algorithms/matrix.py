# w is width, h is height
# Stored in array like this:
# [[w elements] h arrays]

class Matrix:
    def __init__(self, w, h): # Initializes with all zeroes
        self.w = w
        self.h = h
        self.m = [[0] * w for i in range(h)]

    def __add__(self, y):
        assert self.w==y.w and self.h==y.h
        n = Matrix(self.w, self.h)
        for i in range(self.h):
            for j in range(self.w):
                n.m[i][j] = self.m[i][j] + y.m[i][j]
        return n

    def __mul__(self, y): # n cubed implementation
        assert self.w==y.h
        n = Matrix(y.w, self.h)
        for i in range(self.h):
            for j in range(y.w):
                v = 0
                for k in range(self.w):
                    v += self.m[i][k] * y.m[k][j]
                n.m[i][j] = v
        return n

    def __mod__(self, m):
        n = Matrix(self.w, self.h)
        for i in range(self.h):
            for j in range(self.w):
                n.m[i][j] = self.m[i][j] % m
        return n

import copy
def exp(b, e, m):
    assert b.w==b.h
    a = Matrix(b.w, b.h)
    for i in range(a.w):
        a.m[i][i] = 1
    while e > 0:
        if e & 1: a = (a*b)%m
        b = (b*b)%m
        e >>= 1
    return a
