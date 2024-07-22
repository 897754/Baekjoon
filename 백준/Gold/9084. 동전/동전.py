import sys

T = int(sys.stdin.readline())
for play in range(T):
    N = int(sys.stdin.readline())

    coins = []
    input = sys.stdin.readline().split()
    for i in range(N):
        coins.append(int(input[i]))


    M = int(sys.stdin.readline())

    # 로직 구현
    dp = [0]*(M+1)

    for coin in range(N):
        curCost = coins[coin]
        for j in range(1, M+1):
            if j < curCost:
                continue
            if j == curCost:
                dp[j] += 1
                continue
            dp[j] = dp[j-curCost] + dp[j]


    print(dp[M])