from collections import defaultdict, deque

class Node:
    def __init__(self, *e):
        self.edges = defaultdict(int)
        for edge in e: self.edges[edge[0]] = edge[1]
        self.level = -1

class Graph:
    def __init__(self, s, t, *n):
        self.nodes = n
        self.source = n[s]
        self.sink = n[t]

    def reset_levels(self): for node in self.nodes: node.level = -1

def dinics(g):
    maxf = 0
    while True:
        g.reset_levels()
        end = False
        dq = deque()
        dq.append(g.source)
        g.source.level = 0
        while dq:
            cur = dq.popleft()
            for nn, flow in cur.edges.items():
                if flow == 0 or nn.level != -1: continue
                nn.level = cur.level + 1
                if nn == g.sink: end = True
                else: dq.append(nn)
        if not end: return maxf
        while True:
            visited = set()
            end = False
            minf = -1
            curl = 0
            path = deque()
            dq = deque()
            dq.append((g.source, -1))
            while dq and not end:
                cur, curminf = dq.pop()
                visited.add(cur)
                while len(path) > 0 and path[-1].level >= cur.level: path.pop()
                path.append(cur)
                for nn, flow in cur.edges.items():
                    if flow == 0 or nn.level <= cur.level or nn in visited: continue
                    if curminf == -1: curminf = flow
                    else: curminf = min(curminf, flow)
                    if nn == g.sink:
                        maxf += curminf
                        minf = curminf
                        path.append(nn)
                        end = True
                        break
                    else: dq.append((nn, curminf))
            if not end: break
            for i in range(len(path) - 1):
                cur = path[i]
                nn = path[i + 1]
                cur.edges[nn] -= minf
                nn.edges[cur] += minf
                if cur.edges[nn] == 0: del cur.edges[nn]
