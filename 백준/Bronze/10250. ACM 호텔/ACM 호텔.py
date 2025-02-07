import sys

input = sys.stdin.readline

T = int(input())
for _ in range(T):
    H,W,N = map(int, input().split())

    X = (N//H)
    Y = (N%H)

    if(Y == 0):
        Y=H
    else:
        X+=1

    print(f"{Y}{"0" if X < 10 else ""}{X}")