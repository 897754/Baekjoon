import sys

# j M x
# i N y

sys.setrecursionlimit(10**8)

def Search(i,j):
    global count
    count += 1
    visited[i][j] = True
    curTile = inputArr[i][j]
    curX = j
    curY = i
    if curTile == "-":
        while curX+1 < M:
            curX += 1
            if inputArr[curY][curX] != curTile:
                return
            visited[curY][curX] = True

    elif curTile == "|":
        while curY+1 < N:
            curY += 1
            if inputArr[curY][curX]  != curTile:
                return
            visited[curY][curX]  = True
    


input = sys.stdin.readline().split()
N = int(input[0])
M = int(input[1])

visited = [[False]*M for _ in range(N)]
inputArr = []
for i in range(N):
    inputArr.append(sys.stdin.readline().replace("\n",""))

count = 0
for i in range(N):
    for j in range(M):
        if visited[i][j]:
            continue
        Search(i,j)
print(count)