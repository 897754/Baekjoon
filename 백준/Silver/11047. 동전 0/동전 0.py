import sys

input = sys.stdin.readline().split()
N = int(input[0])
K = int(input[1])

coins = []
for i in range(N):
    value = int(sys.stdin.readline())
    if value > K:
        continue
    coins.append(value)

coins.reverse()

count = 0

# 로직 구현
for coin in coins:
    cur = K // coin
    K -= coin * cur
    count += cur
print(count)