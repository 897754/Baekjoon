import sys

N = int(sys.stdin.readline())

arr = [0]
for i in range(N):
    arr.append(int(sys.stdin.readline()))

dp = [0] * (N+1)
dp[1] = arr[1]
if N > 1:
    dp[2] = arr[1]+arr[2]

for i in range(N-1):
    if i + 3 <= N:
        dp[i+3] = dp[i] + arr[i+3] + arr[i+2]
    dp[i+2] = max(dp[i+2], dp[i]+arr[i+2])


print(dp[N])