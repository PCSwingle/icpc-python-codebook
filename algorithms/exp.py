def exp(a, p, m): # a^p % m
    b = bin(p)[2:]
    ans = 1
    na = a
    for i in reversed(b):
        if i == '1':
            ans = (ans * na) % m
        na = (na * na) % m
    return ans
