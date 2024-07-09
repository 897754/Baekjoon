import sys
from collections import deque


def GetNewPos(head, curDir):
    if curDir == 0:
        return (head[0]+1, head[1])
    elif curDir == 1:
        return (head[0], head[1]+1)
    elif curDir == 2:
        return (head[0]-1, head[1])
    else:
        return (head[0], head[1]-1)
def PrintBoard(board, n):
    for y in range(n):
        for x in range(n):
            print(board[x][y],end="")
        print("")

# N : 전체 크기
N = int(sys.stdin.readline())
# K : 사과의 갯수
K = int(sys.stdin.readline())

# 배열 초기화
board = [[0]*N for _ in range(N)]

# 사과 좌표 입력
for i in range(K):
    input = sys.stdin.readline().split()
    board[int(input[1]) - 1][int(input[0]) - 1] = 1


# L : 회전 횟수
L = int(sys.stdin.readline())


rotArr = deque()
# 이동 방향 입력
for i in range(L):
    input = sys.stdin.readline().split()
    # D : 1
    # L : -1
    r = 0
    if input[1] == "D":
        r = 1
    else:
        r = -1
    rotArr.append((int(input[0]), r))

# 0 : 오른쪽
# 1 : 아래쪽
# 2 : 왼쪽
# 3 : 위쪽
curDir = 0

snake = deque()
snake.append((0,0))

time = 0
dirIndex = 0
while True:
    time += 1
    newPos = GetNewPos(snake[0], curDir)
    #print(newPos)
    # 패배 조건
    if newPos[0] < 0 or newPos[1] < 0 or newPos[0] == N or newPos[1] == N or newPos in snake:
        break
    # 사과 체크
    if board[newPos[0]][newPos[1]] != 1:
        snake.pop()
    board[newPos[0]][newPos[1]] = 0
    snake.appendleft(newPos)

    # 회전 체크
    if 0 < len(rotArr):
        if rotArr[0][0] == time:
            curDir = (curDir+rotArr[0][1]+4)%4
            rotArr.popleft()


#PrintBoard(board, N)

print(time)