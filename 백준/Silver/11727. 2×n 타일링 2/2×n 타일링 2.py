import sys

input = sys.stdin.readline

N = int(input())

arr = [1,3,5]

if(N < 3):
    print(arr[N-1])
else:
    for i in range(3,N):
        arr.append(arr[i-1] + arr[i-2] + arr[i-2])
    print(arr[-1] % 10007)