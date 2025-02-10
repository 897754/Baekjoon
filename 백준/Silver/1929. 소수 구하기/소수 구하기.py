import sys


input = sys.stdin.readline

M,N = map(int, input().split())

flag = False
arr = []
for i in range(N+1):
    arr.append(flag)
    flag = not flag
arr[1] = False
arr[2] = True

for i in range(3,N+1,2):
    if(not arr[i]):
        continue
    for j in range(i*2, N+1, i):
        arr[j] = False

for i in range(M, N+1):
    if(arr[i]):
        print(i)