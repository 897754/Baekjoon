import sys

input = sys.stdin.readline

N,M = map(int, input().split())

arr = []

def Check(x, y):
    result0 = 0
    result1 = 0
    for i in range(x,x+8):
        for j in range(y,y+8):
            if((arr[i][j] == 'B') == ((i+j)%2==1)):
                result0 += 1
            if((arr[i][j] == 'W') == ((i+j)%2==1)):
                result1 += 1

    #print(f"({x},{y}) result0:{result0},  result1:{result1}")
    return min(result0, result1)


for i in range(N):
    arr.append(input().rstrip())

result = Check(0,0)
for i in range(N - 7):
    for j in range(M - 7):
        result = min(result,Check(i,j))

print(result)