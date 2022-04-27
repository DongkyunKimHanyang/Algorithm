from collections import deque
def BFS(graph,v,visited):
    q = deque()
    q.append(v)
    while q:
        v = q.popleft()
        print(v, end = ' ')
        for next_node in graph[v]:
            if not visited[next_node]:
                q.append(next_node)
                visited[next_node] = True

