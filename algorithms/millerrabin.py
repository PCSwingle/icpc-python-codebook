import random
def exp(a, p, m):
    b = bin(p)[2:]
    ans = 1
    na = a
    for i in reversed(b):
        if i == '1': ans = (ans * na) % m
        na = (na * na) % m
    return ans

def miller_rabin(n, k=10): # k tests on n
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
