import heapq
import sys
INF = sys.maxsize
input = sys.stdin.readline
n,m = map(int,input().split())
start = int(input())
graph = [[] for i in range(n+1)]
distance = [INF] * (n+1)

for _ in range(n):
    a, b, c = map(int,input())
    graph[a].append((b,c))

def dijkstra(start):
    q=[]
    heapq.heappush(q,(0,start))
    distance[start] = 0
    while q:
        current_dist, current_node = heapq.heappop(q)
        if distance[current_node] < current_dist:
            continue
        for next_node, next_dist in graph[current_node]:
            cost = current_dist + next_dist
            if cost < distance[next_node]:
                distance[next_node] = cost
                heapq.heappush(q,(cost,next_node))

dijkstra(start)

for i in range(1, n+1):
    if distance[i] == INF:
        print("INFINITY")
    else:
        print(distance[i])