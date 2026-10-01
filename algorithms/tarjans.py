# setup: graph is a list of sets (connections)
graph = [set()]

k = len(graph)
stack = []
ids = [-1] * k
low = [-1] * k
onstack = [False] * k
ci = [0]
components = []
def tarjan(v):
    ids[v] = ci[0]
    low[v] = ci[0]
    ci[0] += 1
    stack.append(v)
    onstack[v] = True
    for w in graph[v]:
        if ids[w] == -1:
            tarjan(w)
            low[v] = min(low[v], low[w])
        elif onstack[w]:
            low[v] = min(low[v], ids[w])

    if low[v] == ids[v]:
        c = []
        w = stack.pop()
        while w != v:
            c.append(w)
            onstack[w] = False
            w = stack.pop()
        c.append(w)
        onstack[w] = False
        components.append(c)

for v in range(k):
    if ids[v] == -1:
        tarjan(v)