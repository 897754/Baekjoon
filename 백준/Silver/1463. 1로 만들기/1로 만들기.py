import sys
import math

input = sys.stdin.readline

N = int(input())

dp = [math.inf]*(N+1)
dp[0] = 0
dp[1] = 0

for i in range(1, N+1):
    curI = i + 1
    if(curI <= N):
        dp[curI] = min(dp[curI], dp[i]+1)
    curI = i * 2
    if(curI <= N):
        dp[curI] = min(dp[curI], dp[i]+1)
    curI = i * 3
    if(curI <= N):
        dp[curI] = min(dp[curI], dp[i]+1)

print(dp[N])