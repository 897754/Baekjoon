import sys

input = sys.stdin.readline

N = int(input())

DP = [1,2,4]
for _ in range(N):
    cur = int(input())
    while(len(DP) < cur):
        DP.append(DP[-1]+DP[-2]+DP[-3])
    print(DP[cur-1])