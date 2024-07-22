import sys
from typing import List

def printArr():
    for i in range(N+1):
        for j in range(K+1):
            print(dp[i][j], end="")
        print("")

class Item:
    def __init__(self, weight, value) -> None:
        self.weight = weight
        self.value = value

input = sys.stdin.readline().split()
N = int(input[0])
K = int(input[1])

items:List[Item] = []
for i in range(N):
    input = sys.stdin.readline().split()
    # if int(input[0]) > K:
    #     continue
    items.append(Item(int(input[0]),int(input[1])))

dp = [[0]*(K+1) for _ in range(N+1)]

for i in range(1, N+1):
    for j in range(1, K+1):
        cur = items[i-1]
        if j < cur.weight:
            dp[i][j] = dp[i-1][j]
            continue
        dp[i][j] = max(dp[i-1][j], dp[i-1][j-cur.weight]+cur.value)


print(dp[N][K])