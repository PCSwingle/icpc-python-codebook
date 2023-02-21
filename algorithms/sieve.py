import math
def sieve(l): # primes below l (exclusive)
    isprime = [True] * l
    isprime[0] = False
    isprime[1] = False
    primes = []
    for i in range(l):
        if not isprime[i]: continue
        primes.append(i)
        for j in range(i, math.ceil(l/i)): isprime[i*j] = False
    return primes
