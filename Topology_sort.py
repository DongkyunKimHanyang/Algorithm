import sys
#DAG에서 모든 노드를 방향성에 거스르지 않도록 순서대로 나열하는 알고리즘
from collections import deque

v,e = map(int,input().split())
indegree = [0] * (v+1)
graph = [[]for _ in range(v+1)]

for _ in range(e):
    a,b = map(int,input().split())
    graph[a].append(b)
    indegree[b] += 1


result = []
q = deque()
for i in range(1, v + 1):
    if indegree[i] == 0:
        q.append(i)

while q:
    now = q.popleft()
    result.append(now)

    for i in graph[now]:
        indegree[i] -= 1
        if indegree[i] == 0:
            q.append(i)

for i in result:
    print(i, end = ' ')
