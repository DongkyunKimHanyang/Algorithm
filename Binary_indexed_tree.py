import sys

input = sys.stdin.readline

n, m, k = map(int,input().split())

arr = [0] * (n+1)
tree = [0] * (n+1)

def prefix_sum(i): #i 번째 까지 누적합 계산
    result = 0
    while i > 0:
        result += tree[i]
        i -= (i&-i)
    return result

def update(i, dif): #i 번째 수를 dif 만큼 더하는 함수
    while i <= dif:
        tree[i] += dif
        i += (i & -i)

def interval_sum(start,end):
    return prefix_sum(end) - prefix_sum(start - 1)

for i in range(m + k):
    a,b,c = map(int,input().split())
    if a == 1:
        update(b, c - arr[b])
        arr[b] = c
    else:
        print(interval_sum(b,c))