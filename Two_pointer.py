import sys
#특정한 합을 가지는 부분 연속 수열 찾기

n = 5 #데이터 개수
m = 5 #타겟 값
data = [1,2,3,2,5]

count = 0
interval_sum = 0
end = 0

for start in range(n):
    while interval_sum < m and end < n:
        interval_sum += data[end]
        end += 1
    if interval_sum == m:
        count += 1
    interval_sum -= data[start]

print(count)