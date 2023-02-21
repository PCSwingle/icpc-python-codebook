import matrix, exp, convexhull, dinics, sieve, millerrabin, unionfind

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
    a, b = 21398, 3490 # random numbers
    assert exp.exp(a, b, M) == pow(a, b, M)

def test_convexhull():
    # todo: add convex hull tests
    pass

def test_dinics():
    # todo: refactor dinics + make tests
    pass

def test_sieve():
    # todo: add prime sieve tests
    pass

def test_millerrabin():
    # todo: test millerrabin
    pass

def test_unionfind():
    # todo: test unionfind

if __name__ == "__main__":
    test_matrix()
    test_exp()
    test_convexhull()
    test_dinics()
    test_sieve()
    test_millerrabin()
    test_unionfind()

    print("Tests passed!")
