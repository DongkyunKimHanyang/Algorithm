
#top down
d= [0] * 100

def fibo(x):
    if x ==1 or x==2:
        return 1
    if d[x] != 0:
        return d[x]
    d[x] = fibo(x-1) + fibo(x-2)
    return d[x]

#bottom up
d= [0] * 100
d[1] = 1
d[2] = 1
n=99
for i in range(3,n+1):
    d[i] = d[i-1] + d[i-2]

#LIS

array = [1,3,5,2,4,5]
dp = [1] * len(array)
for i in range(1, len(array)):
    for j in range(i):
        if array[j] < array[i]:
            dp[i] = max(dp[i],dp[j]+1)
print(max(dp))