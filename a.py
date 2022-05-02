import sys
from copy import deepcopy
input = sys.stdin.readline
INF = sys.maxsize

N = int(input())

graph = [[INF]*(N+1)for _ in range(N+1)]

for i in range(1,N+1):
    edges = list(map(int,input().split()))
    for j,e in enumerate(edges):
        if e == 1:
            graph[i][j+1] = 1



for k in range(1,N+1):
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            graph[i][j] = min(graph[i][j],graph[i][k]+graph[k][j])

for i in range(1, N + 1):
    for j in range(1, N + 1):
        if graph[i][j] == INF:
            print(0,end=" ")
        else:
            print(1, end=" ")
    print()
