import random
from exp import exp

def millerrabin(n, k=10): # k tests on n
    if n <= 1: return False
    elif n <= 3: return True
    elif n % 2 == 0: return False
    s = 0
    d = n - 1
    while d % 2 == 0:
        s += 1
        d //= 2
    for _ in range(k):
        a = random.randint(2, n - 1)
        x = exp(a, d, n)
        if x == 1 or x == n - 1: continue
        for _ in range(s - 1):
            x = pow(x, 2, n)
            if x == n - 1: break
        else: return False
    return True
