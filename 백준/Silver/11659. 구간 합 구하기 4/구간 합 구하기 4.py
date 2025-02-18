import sys

input = sys.stdin.readline

N, M = map(int, input().split())

arr = list(map(int, input().split()))
sumArr = [arr[0]]
for i in range(1,N):
    sumArr.append(sumArr[-1] + arr[i])

for _ in range(M):
    l, r = map(int, input().split())
    result = sumArr[r-1]
    if(l > 1):
        result -= sumArr[l-2]
    print(result)
