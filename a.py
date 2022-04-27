import sys



def bfs(x,y):
    dir_x_odd = [-1, -1, 0, 0, 1, 1]
    dir_y_odd = [0, 1, -1, 1, 0, 1]

    dir_x_even = [-1, -1, 0, 0, 1, 1]
    dir_y_even = [1, 0, -1, 1, -1, 0]

    graph = [[0] * 1000 for _ in range(1000)]
    visited = [[False] * 1000 for _ in range(1000)]

    from collections import deque
    q = deque([(x,y)])
    visited[x][y] = True
    while q:
        x,y = q.popleft()

        if x % 2 == 0:
            dx = dir_x_even
            dy = dir_y_even
        else:
            dx = dir_x_odd
            dy = dir_y_odd

        for i in range(6):
            next_x = x + dx[i]
            next_y = y + dy[i]

            if 0<=next_x<1000 and 0<=next_y<1000:
                if visited[next_x][next_y]:
                    continue
                visited[next_x][next_y] = True
                q.append((next_x,next_y))
                graph[next_x][next_y] = graph[x][y] + 1
    return graph

start_x, start_y = 381,663

graph = bfs(start_x, start_y)

print(graph[655][845])


