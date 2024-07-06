import sys


arr = []
for i in range(9):
    arr.append(int(sys.stdin.readline()))

# 총합 계산
sum = 0
for i in arr:
    sum+=i

diff = sum - 100

bo = True

i = 0
j = 0
for i in range(9):
    for j in range(1, 9-i):
        if arr[i] + arr[i+j] == diff:
            bo = False
            break
    if not bo:
        break

arr.remove(arr[j+i])
arr.remove(arr[i])
arr.sort()

for i in arr:
    print(i)