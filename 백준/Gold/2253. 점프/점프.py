import sys
from collections import deque 

def printDPs():
    for i in range(N):
        print(f"{i} : ", end="")
        keys = list(dp[i].keys())
        for j in keys:
            print(f"{j},{dp[i][j]}", end=" ")
        print("")

input = sys.stdin.readline().split()
N = int(input[0])
M = int(input[1])

obstacles = {}
dp = [{} for _ in range(N)]
for i in range(M):
    obstacles[int(sys.stdin.readline())-1] = True

# Dictionary[speed] = count
if 0 not in obstacles and 1 not in obstacles:
    dp[0][0] = 0
# i : 여기서 갈 수 있는 돌 메모
for i in range(N):
    curDPs = dp[i]
    # j : 여기가 갈 수 있는지 체크
    for j in curDPs:
        curSpeed = j
        curCount = curDPs[j]
        for k in range(j-1, j+2):
            if k < 1 or i+k >= N:
                continue
            if i+k in obstacles:
                continue

            curTarget = dp[i+k]
            if k in curTarget:
                if curTarget[k] > curCount+1:
                    curTarget[k] = curCount+1
            else:
                curTarget[k] = curCount+1


#printDPs()

if dp[N-1]:
    key = list(dp[-1].keys())[0]
    print(dp[-1][key])
else:
    print(-1)