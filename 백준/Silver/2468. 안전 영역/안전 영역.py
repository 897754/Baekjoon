import sys
sys.setrecursionlimit(10**8)

def Sink(heightArr, n, height):

       
    sunkArr = []

    for i in range(n):
        sunkArr.append([])
        for j in range(n):
            sunkArr[i].append(0)

    for x in range(n):
        for y in range(n):
            if heightArr[x][y] <= height:
                sunkArr[x][y] = 1
    
    #PrintArr(sunkArr)
    
    #탐색할 배열 초기화
    checkArr = []
    for i in range(n):
        checkArr.append([])
        for j in range(n):
            checkArr[i].append(0)

    #탐색 시작
    count = 0
    for x in range(n):
        for y in range(n):
            #잠기지 않았고 확인하지 않은 위치 발견
            if not checkArr[x][y] and not sunkArr[x][y]:
                count+=1
                PaintArea(checkArr, sunkArr, x,y,n)

    return count

def PaintArea(checkArr, sunkArr, x,y,n):
    checkArr[x][y] = 1
    
    curX = 0+x
    curY = 1+y
    if curX >= 0 and curX < n and curY >= 0 and curY < n and not checkArr[curX][curY] and not sunkArr[curX][curY]:
        PaintArea(checkArr,sunkArr,curX,curY,n)
    curX = 0+x
    curY = -1+y
    if curX >= 0 and curX < n and curY >= 0 and curY < n and not checkArr[curX][curY] and not sunkArr[curX][curY]:
        PaintArea(checkArr,sunkArr,curX,curY,n)
    curX = 1+x
    curY = 0+y
    if curX >= 0 and curX < n and curY >= 0 and curY < n and not checkArr[curX][curY] and not sunkArr[curX][curY]:
        PaintArea(checkArr,sunkArr,curX,curY,n)
    curX = -1+x
    curY = 0+y
    if curX >= 0 and curX < n and curY >= 0 and curY < n and not checkArr[curX][curY] and not sunkArr[curX][curY]:
        PaintArea(checkArr,sunkArr,curX,curY,n)




def PrintArr(arr):
    for i in arr:
        print(i)


n = int(sys.stdin.readline())

heightArr = []
for i in range(n):
    heightArr.append([])
    input = sys.stdin.readline().split()
    for j in range(n):
        heightArr[i].append(int(input[j]))

max = 0
for i in range(100):
    cur = Sink(heightArr, n, i)
    if max < cur:
        max = cur
print(max)