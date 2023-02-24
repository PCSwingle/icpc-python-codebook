import math, random

def exp(b, e, m):
    a = 1
    while e > 0:
        if e & 1: a = (a*b)%m
        b = (b*b)%m
        e >>= 1
    return a

def pollardrho(n): # returns ONE prime divisor of n
    if (n == 1): return n
    if (n % 2 == 0): return 2

    x = random.randint(0, n-1)
    y = x
    c = random.randint(1, n-1)
    d = 1
    while d == 1:
        x = (exp(x, 2, n)+c+n)%n
        y = (exp(y, 2, n)+c +n)%n
        y = (exp(y, 2, n)+c+n)%n
        d = math.gcd(abs(x-y), n)
        if (d == n): return PollardRho(n)
    return d
