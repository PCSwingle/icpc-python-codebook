import math, sys, random

import matrix, exp, convexhull, dinics, sieve, millerrabin, unionfind, pollardrho

M = 1_000_000_007

def test_matrix():
    # Use fibonacci exponentiation by squaring to test
    mat = matrix.Matrix(2, 2)
    mat.m = [[1, 1], [1, 0]]
    start = matrix.Matrix(1, 2)
    start.m = [[1], [0]]
    ans = matrix.exp(mat, 100, M) * start

    fib = 573147844013817084101 # 101 fibonacci number
    assert ans.m[0][0] == fib % M

def test_exp():
    for i in range(100):
        a, b = random.randint(0, 10000), random.randint(0, 10000)
        assert exp.exp(a, b, M) == pow(a, b, M)

def test_convexhull():
    # use kattis convexhull as test case: currently passes
    #while (n := int(input())) != 0:
    #    points = [tuple(map(int, input().split())) for i in range(n)]
    #    hull = convexhull.convex_hull(points)
    #    print(len(hull))
    #    for p in hull:
    #        print(p[0], p[1])
    pass

def test_dinics():
    # todo: refactor dinics + make tests -- either way python is probably too slow for max flwo no matter what
    pass

def test_sieve():
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    assert sieve.sieve(100) == primes
    pass

def test_millerrabin():
    ps = [48112959837082048697, 54673257461630679457, 29497513910652490397, 40206835204840513073, 12764787846358441471, 71755440315342536873, 45095080578985454453, 27542476619900900873, 66405897020462343733, 36413321723440003717]
    nps = [48112959837082048699, 54673257461630679459, 29497513910652490401, 40206835204840513075, 12764787846358441473, 71755440315342536875, 45095080578985454455, 27542476619900900875, 66405897020462343735, 36413321723440003719]
    for p in ps:
        assert millerrabin.millerrabin(p, 20)
    for np in nps:
        assert not millerrabin.millerrabin(np, 20)
    pass

def test_unionfind():
    # use kattis unionfind as test case: currently passes
    #lines = sys.stdin.readlines()
    #n, q = map(int, lines[0].split())
    #s = UnionFind(n)
    #for i in range(q):
    #    line = lines[i + 1].split()
    #    if line[0] == '=':
    #        s.merge(int(line[1]), int(line[2]))
    #    else:
    #        if s.query(int(line[1]), int(line[2])):
    #            print('yes')
    #        else:
    #            print('no')
    pass

def test_pollardrho():
    primes = sieve.sieve(100000)
    comps = []
    for i in range(50):
        p1 = primes[random.randint(0, len(primes) - 1)]
        p2 = primes[random.randint(0, len(primes) - 1)]
        p3 = primes[random.randint(0, len(primes) - 1)]
        comps.append((p1*p2*p3, p1, p2, p3))
    for c in comps:
        assert pollardrho.pollardrho(c[0]) in c
    pass

if __name__ == "__main__":
    test_matrix()
    test_exp()
    test_convexhull()
    test_dinics()
    test_sieve()
    test_millerrabin()
    test_unionfind()
    test_pollardrho()

    print("Tests passed!")
