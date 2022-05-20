import sys
#음수 간선이 포함되었을때 최단거리 구하는데 사용. 다익스트라보다 높은 시간복잡도
input = sys.stdin.readline
INF = int(1e9)

n,m = map(int,input().split())
start = int(input())
edges = []
dist = [INF] * (n+1)

for _ in range(m):
    a, b, c = map(int, input().split())
    edges.append((a,b,c))

negative_cycle = False
dist[start] = 0

for i in range(n):
    for j in range(m):
        for current_node, next_node, weight in edges:
            if dist[current_node] != INF and dist[next_node] > dist[current_node] + weight:
                dist[next_node] = dist[current_node] + weight
                if i == n-1:
                    negative_cycle= True