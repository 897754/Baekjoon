import sys

input = sys.stdin.readline

def Search(x, y):
    if(dp[x][y] >= 0):
        return dp[x][y]

    result = (Search(x-1, y) + Search(x, y-1))
    dp[x][y] = result
    return result

T = int(input())

dp = [[-1] * 15 for _ in range(15)]

for i in range(15):
    dp[0][i] = 0
    dp[i][0] = i


for _ in range(T):
    k = int(input())
    n = int(input())
    print(Search(n,k))
    