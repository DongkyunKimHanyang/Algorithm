def dfs(graph,v,visited):
    visited[v] = True
    print(v, end=' ')
    for next_node in graph[v]:
        if not visited[next_node]:
            dfs(graph,next_node,visited)