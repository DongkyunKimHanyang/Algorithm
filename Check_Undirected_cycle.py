import sys
#무방향 그래프에서 cycle이 있는지 체크하는 알고리즘
def find_parent(parent,x):#루트 찾기
    if parent[x] !=x:
        parent[x] = find_parent(parent,parent[x])
    return parent[x]

def union_parent(parent,a,b):#두 노드의 루트 동일하게 만들기 (합집합 연산)
    a = find_parent(parent,a)
    b = find_parent(parent,b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


v, e = map(int, input().split())
parent = [0] * (v+1)

for i in range(1, v+1):
    parent[i] = i

cycle = False
for i in range(e):
    a,b = map(int,input().split())
    if find_parent(parent,a) == find_parent(parent,b): #두 노드의 루트가 같다면(같은 집합에 포함되어있다면) Cycle이 있는것
        cycle = True
    else:
        union_parent(parent,a,b)

