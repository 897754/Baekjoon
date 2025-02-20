import sys

input = sys.stdin.readline

N = int(input())

arr = [1,2]

if(N < 3):
    print(arr[N-1])
else:
    for i in range(2,N):
        arr.append(arr[i-1] + arr[i-2])
    print(arr[-1] % 10007)