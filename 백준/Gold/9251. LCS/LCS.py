import sys

def printArr():
    for i in range(a+1):
        for j in range(b+1):
            print(dp[i][j], end="")
        print("")

A = sys.stdin.readline().rstrip()
B = sys.stdin.readline().rstrip()


a = len(A)
b = len(B)
dp = [[0]*(b+1) for _ in range(a+1)]

for i in range(1, a+1):
    for j in range(1, b+1):
        if A[i-1] == B[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i][j-1], dp[i-1][j])

print(dp[a][b])