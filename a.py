
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

for i in range(n):
for i,edge in enumerate(edges):
    curr_node, next_node, cost = edge
    if distance[curr_node] != INF and distance[curr_node] + cost < distance[next_node]:
        distance[next_node] = distance[curr_node] + cost
        if i == N-1:
            negative_cycle = True

if negative_cycle:
    print(-1)
    exit()
else:
    for d in distance[2:]:
        if d == INF:
            print(-1)
        else:
            print(d)

