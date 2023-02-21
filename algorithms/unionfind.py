class UnionFind:
    def __init__(self, n):
        self.data = [i for i in range(n)]

    def get_root(a):
        l = 0
        while data[a] != a:
            data[a] = data[data[a]]
            a = data[a]
            l += 1
        return (a, l)

    def merge(a, b):
        ar, al = get_root(a)
        br, bl = get_root(b)
        if al < bl: data[ar] = br
        else: data[br] = ar

    def query(a, b):
        ar, al = get_root(a)
        br, bl = get_root(b)
        return ar == br
