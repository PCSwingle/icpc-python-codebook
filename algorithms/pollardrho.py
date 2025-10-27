import math, random
from millerrabin import millerrabin
from exp import exp

def pollardrho(n): # returns ONE not-necessarily-prime divisor of n
    if (n == 1): return n
    if (n % 2 == 0): return 2
    if millerrabin(n): return n

    x = random.randint(0, n-1)
    y = x
    c = random.randint(1, n-1)
    d = 1
    while d == 1:
        x = (exp(x, 2, n)+c+n)%n
        y = (exp(y, 2, n)+c +n)%n
        y = (exp(y, 2, n)+c+n)%n
        d = math.gcd(abs(x-y), n)
        if (d == n): return pollardrho(n)
    return d
