import sys


N = int(sys.stdin.readline())


A = sys.stdin.readline().split()
arr = []
for i in A:
    arr.append(int(i))


dp = [0]*(N)

maxResult = 1
dp[0] = 1
for i in range(1, N):
    maxIndex = -1
    for j in range(i):
        if arr[j] < arr[i] and (maxIndex == -1 or dp[maxIndex] < dp[j]):
            maxIndex = j
    dp[i] = dp[maxIndex] + 1
    if maxIndex == -1:
        continue
    if dp[i] > maxResult:
        maxResult = dp[i]

print(maxResult)