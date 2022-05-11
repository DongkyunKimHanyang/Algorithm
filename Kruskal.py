import sys
#최소 신장 트리를 만드는 알고리즘
#최소 신장 트리: 모든 노드는 서로 도달이 가능하며 싸이클이 없고 간선 비용의 합이 최소인 그래프
def find_parent(parent,x):#루트 찾기
    if parent[x] !=x:
        parent[x] = find_parent(parent,parent[x])
    return parent[x]
def union_parent(parent,a,b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

v,e = map(int,input().split())
parent = [0] * (v+1)
edges = []
result = 0
for i in range(1, v+1):
    parent[i] = i

for _ in range(e):
    a,b,cost = map(int,input().split())
    edges.append((cost,a,b))
edges.sort() #edge들을 cost 오름 차순으로 정렬

for edge in edges:
    cost, a, b = edge
    if find_parent(parent,a) != find_parent(parent,b):
        union_parent(parent,a,b)
        result += cost

print(result)