import sys
input = sys.stdin.readline

N = int(input())

arr = []
for i in range(N):
    arr.append(list(map(int, input().split())))

result = 0

def DP(arr, y, x):
    global result
    if(x == 0):
        arr[y][x] = arr[y-1][x] + arr[y][x]
    elif(x == y):
        arr[y][x] = arr[y-1][x-1] + arr[y][x]
    else:
        arr[y][x] = max(arr[y-1][x], arr[y-1][x-1]) + arr[y][x]
        
    if y == N-1:
        if x == 0:
            result = arr[y][x]
        elif result < arr[y][x]:
            result = arr[y][x]
            

if(N == 1):
    result = arr[0][0]
for i in range(1,N):
    for j in range(i+1):
        DP(arr, i, j)

print(result)