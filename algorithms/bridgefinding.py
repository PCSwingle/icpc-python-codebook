visited = [False] * n
tin = [-1] * n
low = [-1] * n
timer = 0

bridges = []

def dfs(cur, parent):
    global timer
    
    visited[cur] = True
    tin[cur] = timer
    low[cur] = timer
    timer += 1
    
    for to in adj[cur]:
        if to == parent: # change if multiple edges
            continue
        
        if visited[to]:
            low[cur] = min(low[cur], tin[to])
        else:
            dfs(to, cur)
            low[cur] = min(low[cur], low[to])
            if low[to] > tin[cur]:
                bridges.append((cur, to))

for v in range(n):
    if not visited[v]:
        dfs(v, None)