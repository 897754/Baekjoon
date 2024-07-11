import sys
import itertools

sys.setrecursionlimit(10**8) # 10^8 까지 늘림.

result = ""

def Rec(arr, x,y, size):
    global result
    flag = arr[x][y]
    isFull = True
    for i in range(size):
        for j in range(size):
            if flag != arr[x+i][y+j]:
                isFull = False
                break
        if not isFull:
            break
    
    if isFull:
        result += flag
        return
    
    mid = size//2
    result += "("
    Rec(arr, x,y, mid)
    Rec(arr, x,y + mid, mid)
    Rec(arr, x + mid,y, mid)
    Rec(arr, x + mid,y + mid, mid)
    result += ")"



# N : 전체 크기
N = int(sys.stdin.readline())




arr = []
for i in range(N):
    arr.append([])
    input = sys.stdin.readline()
    for j in range(N):
        arr[i].append(input[j])


# 로직 구현
Rec(arr, 0,0,N)


print(result)