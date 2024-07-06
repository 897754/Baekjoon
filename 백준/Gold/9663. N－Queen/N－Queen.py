import copy
import sys

def PrintBoard(n, queenArr):
    arr = []
    for x in range(n):
        arr.append([])
        for y in range(n):
            arr[x].append(0)

    index = 0
    for i in queenArr:
        arr[index][queenArr[index]] = 1
        index+=1
    for i in arr:
        print(i)
    print('')

count = 0
def CheckQueen(x,y,n, queenArr):
    global count

    for curY in range(y):
        # 해당 위치에 퀸을 놓을수 있는지 체크
        if (x == queenArr[curY]) or (abs(queenArr[curY] - x) == abs(curY - y)):
            return
    # 퀸 위치 배열에 현재위치 추가
    queenArr[y] = x
    
    y += 1
    # n-Queen 조건 달성
    if y >= n:
        #PrintBoard(n,queenArr)
        count+=1
        return
    
    # 다음 줄 재귀
    for x in range(n):
        CheckQueen(x,y,n,queenArr)

n = int(sys.stdin.readline())

queenPositions = []
for i in range(n):
    queenPositions.append(None)


for i in range(n):
    CheckQueen(i,0,n,queenPositions)
print(count)