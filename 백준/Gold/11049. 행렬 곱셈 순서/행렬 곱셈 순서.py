import sys

def printArr():
    for i in range(N):
        for j in range(N):
            print("{:3d}".format(dp[i][j]), end="")
        print("")

def MatMul(a,b):
    return a[0]*a[1]*b[1]

N = int(sys.stdin.readline())

arr = []
for i in range(N):
    input = sys.stdin.readline().split()
    arr.append((int(input[0]), int(input[1])))

dp = [[0] * N for _ in range(N)]


for i in range(N-1):
    for j in range(N-1-i):
        if i == 0:
            a = arr[j]
            b = arr[j+1]
            dp[j][j+1] = MatMul(a,b)
            continue
        min = 10000000000
        for k in range(i+1):
            # print(f"k:{k} i:{i} j:{j}")
            a = (arr[j][0],arr[j-k+i][1])
            b = (arr[j-k+2][0],arr[i+j+1][1])
            # print(f"a:{a} b:{b}")

            # print(f"{dp[j][i+j-k]} + {dp[i+j-k+1][i+j+1]}")
            val = MatMul(a,b) + dp[j][i+j-k] + dp[i+j-k+1][i+j+1]
            #dp[j][i+j+1]
            if min > val:
                min = val
        # print(f"min : {min}")
            
        dp[j][i+j+1] = min


print(dp[0][N-1])