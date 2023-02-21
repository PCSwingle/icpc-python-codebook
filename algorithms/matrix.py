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
def exp(a, p, m): # a^p % m, must be square matrix
    assert a.w==a.h
    b = bin(p)[2:]
    ans = Matrix(a.w, a.h)
    for i in range(a.w):
        ans.m[i][i] = 1
    na = copy.deepcopy(a)
    for i in reversed(b):
        if i == '1':
            ans = (ans * na) % m
        na = (na * na) % m
    return ans
