import sys
input = sys.stdin.readline

N, M = map(int, input().split())

arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))


i1 = 0
i2 = 0

while(i1 < N and i2 < M):
    if(arr1[i1] < arr2[i2]):
        print(arr1[i1], end=" ")
        i1+=1
    else:
        print(arr2[i2], end=" ")
        i2+=1

if(i1 < N):
    while(i1 < N):
        print(arr1[i1], end=" ")
        i1+=1
else:
    while(i2 < M):
        print(arr2[i2], end=" ")
        i2+=1