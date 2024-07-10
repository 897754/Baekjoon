import sys
def dac(a, b, c):
    if b == 1:
        return a % c
    elif b % 2 == 0:
        return (dac(a,b//2,c)**2)%c
    else:
        return ((dac(a,b//2,c)**2)*a)%c

def matPow(a, B, N):
    if B == 0:
        arr = [[0]*N for _ in range(N)]
        for i in range(N):
            arr[i][i] = 1
        return arr
    if B == 1:
        for i in range(N):
            for j in range(N):
                a[i][j] %= 1000
        return a
    
    temp = matPow(a, B//2,N)
    if B % 2 == 0:
        return matMul(temp, temp, N)
    else:
        return matMul(a, matMul(temp, temp, N), N)
    
def matMul(a,b,N):
    result = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            sum = 0
            for k in range(N):
                sum += a[i][k] * b[k][j]
            result[i][j] = sum % 1000
    return result

# N : 전체 크기
input = sys.stdin.readline().split()
N = int(input[0])
B = int(input[1])

arr = []
for i in range(N):
    input = sys.stdin.readline().split()
    arr.append([])
    for j in range(N):
        arr[i].append(int(input[j]))

result = (matPow(arr, B, N))

for i in result:
    for j in i:
        print(j, end=" ")
    print("")