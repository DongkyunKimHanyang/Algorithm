
import sys
INF = sys.maxsize
input = sys.stdin.readline

N, E = map(int, input().split())

edges=[]

for _ in range(E):
    a,b,c = map(int,input().split())
    edges.append((a,b,c))

distance = [INF] * (N + 1)
negative_cycle = False
distance[1] = 0

for i in range(N):
    for j in range(E):
        for edge in edges:
            curr_node, next_node, cost = edge
            if distance[curr_node] != INF and distance[curr_node] + cost < distance[next_node]:
                distance[next_node] = distance[curr_node] + cost
                if i == N-1:
                    negative_cycle = True

if negative_cycle:
    print(-1)
else:
    for i in range(2, N + 1):
        # 도달할 수 없는 경우
        if distance[i] == INF:
            print(-1)
        # 도달 가능한 경우
        else:
            print(distance[i])
