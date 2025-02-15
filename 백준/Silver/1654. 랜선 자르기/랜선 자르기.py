import sys

def calc(arr, value):
    sum = 0
    for a in arr:
        sum += a//value
    return sum

input = sys.stdin.readline

K,N = map(int, input().split())

max = 0
arr = []
for _ in range(K):
    cur = int(input())
    if(max < cur):
        max = cur
    arr.append(cur)

left = 0
right = max
max = 0
while(left+1 < right):
    mid = (left + right) // 2
    if(calc(arr, mid) < N):
        right = mid
    else:
        left = mid
        max = mid

mid = right
if(calc(arr, mid) >= N):
    max = mid
print(max)