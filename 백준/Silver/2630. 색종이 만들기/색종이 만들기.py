import sys

count0 = 0
count1 = 0

def DivideBoard(board, start, end):
    global count0
    global count1
    color = board[start[0]][start[1]]

    if start == end:
        if color:
            count1 += 1
        else:
            count0 += 1
        return
    if start[0]+1 == end[0] and start[1]+1 == end[1]:
        if color:
            count1 += 1
        else:
            count0 += 1
        return

    result = True
    for i in range(start[0], end[0]):
        for j in range(start[1], end[1]):
            if board[i][j] != color:
                result = False
                break
        if not result:
            break
    if result:
        if color:
            count1 += 1
        else:
            count0 += 1
        return

    #재귀
    midX = (start[0]+end[0])//2
    midY = (start[1]+end[1])//2
    DivideBoard(board, start, (midX,midY))
    DivideBoard(board, (midX, start[1]),(end[0],midY))
    DivideBoard(board, (start[0], midY),(midX,end[1]))
    DivideBoard(board, (midX, midY),(end[0],end[1]))


# N : 전체 크기
N = int(sys.stdin.readline())

    
# 배열 크기만큼 좌표 입력
board = []
for i in range(N):
    board.append([])
    input = sys.stdin.readline().split()
    for j in input:
        board[i].append(int(j))
        

# 여기서부터 로직 시작0

DivideBoard(board, (0,0), (N,N))

print(count0)
print(count1)