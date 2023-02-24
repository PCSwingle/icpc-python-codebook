class UnionFind:
    def __init__(self, n):
        self.data = [i for i in range(n)]

    def get_root(self, a):
        l = 0
        while self.data[a] != a:
            self.data[a] = self.data[self.data[a]]
            a = self.data[a]
            l += 1
        return (a, l)

    def merge(self, a, b):
        ar, al = self.get_root(a)
        br, bl = self.get_root(b)
        if al < bl: self.data[ar] = br
        else: self.data[br] = ar

    def query(self, a, b):
        ar, al = self.get_root(a)
        br, bl = self.get_root(b)
        return ar == br
